
from CLI.commands.base import Command


class Update(Command):
    name = "update"
    help = "Updates a task"

    def add_arguments(self, parser):
        parser.add_argument("--id", type=int)
        parser.add_argument("--desc", default="")

    def handle(self, args, service):
        service.update(args.id, args.desc)
