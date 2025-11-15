import argparse
from core.service import TaskService
from CLI.commands.add import AddCommand
from CLI.commands.list import List
from CLI.commands.done import Done
from CLI.commands.delete import Delete


class TaskCLI:
    def __int__(self):
        self.service = TaskService()
        self.parser = argparse.ArgumentParser(description="Taskit")
        subparsers = self.parser.add_subparsers(dest="command")

        self.commands = [
            AddCommand(),
            List(),
            Done(),
            Delete(),
        ]

        for cmd in self.commands:
            cmd.register(subparsers)

    def run(self):
        args = self.parser.parse_args()

        if not hasattr(args, "handler"):
            self.parser.print_help()
            return

        args.handler(args, self.service)
