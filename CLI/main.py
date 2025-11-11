import argparse
from core.task_manager import add, list_tasks, mark_complete, delete
from core.database import init_db


def main():
    init_db()

    parser = argparse.ArgumentParser(description="TaskMe - CLI Task Manager")

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")

    add_parser.add_argument("title", help="Title of the task")
    add_parser.add_argument("--desc", help="Description", default="")
    add_parser.add_argument("--due", help="Due-date", default=None)
    add_parser.add_argument("--tag", help="Tage", default=None)

    subparsers.add_parser("list")

    done_parser = subparsers.add_parser("done")
    done_parser.add_argument("id", type=int, help="Task ID")

    del_parser = subparsers.add_parser("del")
    del_parser.add_argument("id", type=int, help="Task ID")

    args = parser.parse_args()

    if args.command == "add":
        add(args.title, args.desc, args.due, args.tag)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        mark_complete(args.id)
    elif args.command == "del":
        delete(args.id)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()