from core.task_manager import TaskRepository
from core.task import Task


class TaskService:
    def __int__(self):
        self.repo = TaskRepository()

    def add(self, title, desc, due, tag):
        task = Task(title, desc, due, tag)
        self.repo.add(task)

    def list(self):
        rows = self.repo.list()
        for row in rows:
            print(f"[{row['id']}] {row['title']} ({row['status']})")

    def done(self, task_id):
        self.repo.mark_done(task_id)

    def delete(self, task_id):
        self.repo.delete(task_id)
