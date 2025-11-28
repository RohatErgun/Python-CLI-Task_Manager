from core.task_manager import TaskRepository
from core.task import Task
from Log.log import LogSystem
from Pomodoro.pomodoro import Pomodoro


class TaskService:
    def __init__(self):
        self.repo = TaskRepository()

    def print_help(self):
        print("\ntask not found\t(-h/--help) for more information")

    def task_exists(self, task_id):
        rows = self.repo.search(task_id=task_id)
        return len(rows) > 0

    @LogSystem.logged
    def add(self, title, desc, due, tag):
        task = Task(title, desc, due, tag)
        task_id = self.repo.add(task)  # DB inserts & returns id
        print(f"Task added with ID {task_id}")

    @LogSystem.logged
    def list(self):
        rows = self.repo.list()
        if not rows:
            print("[ ]")
            return

        for row in rows:
            print(f"[{row['id']}] {row['title']} ({row['status']})")

    @LogSystem.logged
    def done(self, task_id):
        if self.task_exists(task_id):
            self.repo.mark_done(task_id)
            print(f"Task {task_id} marked as done")
        else:
            self.print_help()

    @LogSystem.logged
    def delete(self, task_id):
        if self.task_exists(task_id):
            self.repo.delete(task_id)
            print(f"Task {task_id} deleted")
        else:
            self.print_help()

    @LogSystem.logged
    def search(self, title=None, task_id=None, tag=None):
        rows = self.repo.search(title, task_id, tag)

        if not rows:
            print("[ ]")
            return

        for row in rows:
            print(
                f"[{row['id']}] {row['title']} {row['description']} "
                f"{row['due_date']} {row['tag']} ({row['status']})"
            )

    @LogSystem.logged
    def update(self, task_id, new_desc):
        if self.task_exists(task_id):
            self.repo.update(task_id, new_desc)
            print(f"Task {task_id} updated")
        else:
            self.print_help()

    """ 
        function logic implemented in Pomodoro/pomodoro.py
        TaskService handles function for more simplistic CLI/main.py  
    """
    @LogSystem.logged
    def pomo(self):
        pomo = Pomodoro()
        pomo.main()
