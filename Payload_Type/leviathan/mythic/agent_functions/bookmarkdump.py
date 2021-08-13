import json

from mythic_payloadtype_container.MythicCommandBase import *


class BookmarkDumpArguments(TaskArguments):
    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = {}

    async def parse_arguments(self):
        pass


class BookmarkDumpCommand(CommandBase):
    cmd = "bookmarkdump"
    needs_admin = False
    help_cmd = "bookmarkdump"
    description = "Dump all bookmarks from the browser"
    version = 1
    author = "@sysop_host"
    argument_class = BookmarkDumpArguments
    attackmapping = []

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        return task

    async def process_response(self, response: AgentResponse):
        pass
