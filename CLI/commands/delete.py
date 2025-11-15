from CLI.commands.base import Command


class Delete(Command):
    name = "delete"
    help = "Delete task"

    def add_arguments(self, parser):
        parser.add_argument("id", type=int)

    def handle(self, args, service):
        service.delete(args.id)
