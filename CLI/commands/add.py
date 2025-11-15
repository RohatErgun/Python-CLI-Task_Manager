
from CLI.commands.base import Command

class AddCommand(Command):
    name = "add"
    help = "Add new task."

    def add_arguments(self, parser):
        parser.add_argument("title")
        parser.add_argument("--desc", default="")
        parser.add_argument("--due", default=None)
        parser.add_argument("--tag", default=None)


    def handle(self, args, service):
        service.add(args.title,
                    args.desc,
                    args.due,
                    args.tag)


