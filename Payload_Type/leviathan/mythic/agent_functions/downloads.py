import json

from mythic_payloadtype_container.MythicCommandBase import *


class DownloadsArguments(TaskArguments):
    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = {}

    async def parse_arguments(self):
        pass


class DownloadsCommand(CommandBase):
    cmd = "downloads"
    needs_admin = False
    help_cmd = "downloads"
    description = "Dump download history"
    version = 1
    author = "@sysop_host"
    argument_class = DownloadsArguments
    browser_script = [BrowserScript(script_name="downloads_parser", author="@sysop_host")]
    attackmapping = []

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        return task

    async def process_response(self, response: AgentResponse):
        pass
