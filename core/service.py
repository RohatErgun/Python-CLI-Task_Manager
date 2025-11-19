from core.task_manager import TaskRepository
from core.task import Task
from Log.log import LogSystem


class TaskService:
    def __init__(self):
        self.repo = TaskRepository()
        self.tasks = {}
        self.id = 1

    def print_help(self):
        print(f"\ntask not found\t(-h/--help) for more information")

    @LogSystem.logged
    def add(self, title, desc, due, tag):
        if title not in self.tasks:
            task = Task(title, desc, due, tag)
            self.repo.add(task)
            self.tasks[title] = self.id
            self.id += self.id
        else:
            print(f"Duplicate {title} found\t(-h/--help) for more information")

    @LogSystem.logged
    def list(self):
        rows = self.repo.list()
        if not rows:
            print("[ ]")
        for row in rows:
            print(f"[{row['id']}] {row['title']} ({row['status']})")

    @LogSystem.logged
    def done(self, task_id):
        if task_id in self.tasks.values():
            self.repo.mark_done(task_id)
        else:
            self.print_help()

    @LogSystem.logged
    def delete(self, task_id):
        if task_id in self.tasks.values():
            self.repo.delete(task_id)
        else:
            self.print_help()

    @LogSystem.logged
    def search(self, title=None, task_id=None, tag=None):
        rows = self.repo.search(title, task_id, tag)

        if not rows:
            print("[ ]")

        for row in rows:
            print(f"[{row['id']}] {row['title']} {row['description']} {row['due_date']} "
                  f"{row['tag']} ({row['status']})")