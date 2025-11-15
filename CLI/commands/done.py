from CLI.commands.base import Command


class Done(Command):
    name = "done"
    help = "Mark the task as done"

    def add_arguments(self, parser):
        parser.add_argument("id", type=int)

    def handle(self, args, service):
        service.done(args.id)