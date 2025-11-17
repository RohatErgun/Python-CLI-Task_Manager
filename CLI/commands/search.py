from CLI.commands.base import Command


class Search(Command):
    name = "search"
    help = "Seach a task"

    def add_arguments(self, parser):
        parser.add_argument("--title", default=None)
        parser.add_argument("--id", type=int, default=None)
        parser.add_argument("--tag", default=None)

    def handle(self, args, service):
        service.search(args.title, args.id, args.tag)
