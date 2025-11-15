
class Command:
    name = ""
    help = ""

    def register(self, subparsers):
        parser = subparsers.add_parser(self.name, help=self.name)
        self.add_arguments(parser)
        parser.set_defaults(handler=self.handle)

    def add_arguments(self, parser):
        pass

    def handle(self, args, service):
        raise NotImplementedError