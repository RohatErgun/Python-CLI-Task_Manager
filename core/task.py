#

class Task:
    def __init__(self, title, description, due_date=None, tag=None, status="pending"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tag = tag
        self.status = status

    def __repr__(self):
        return f"<Task:{self.title}, status={self.status}"

