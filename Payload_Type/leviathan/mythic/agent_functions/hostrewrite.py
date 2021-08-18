from mythic_payloadtype_container.MythicCommandBase import *


class HostRewriteArguments(TaskArguments):
    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = {
            "host": CommandParameter(
                name="host",
                type=ParameterType.String,
                description="Host header to inject",
                required=True,
            ),
        }

    async def parse_arguments(self):
        self.load_args_from_json_string(self.command_line)


class InjectCommand(CommandBase):
    cmd = "hostrewrite"
    needs_admin = False
    help_cmd = 'hostrewrite {"host":"host header value"}'
    description = "Rewrite host header for outgoing requests"
    version = 1
    author = "@sysop_host"
    argument_class = HostRewriteArguments
    attackmapping = []

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        return task

    async def process_response(self, response: AgentResponse):
        pass
