from CLI.commands.base import Command


class List(Command):
    name = "list"
    help = "List tasks based on task_id"

    def handle(self, args, service):
        service.list()
