from core.database import get_connection

# Encapsulates SQL

class TaskRepository:
    def add(self, task):
        with get_connection() as conn:
            conn.execute("INSERT INTO tasks (title, description, due_date, tag) "
                         "VALUES (?, ?, ?, ?)",
                         (task.title, task.description, task.due_date, task.tag))
            conn.commit()

    def list(self):
        with get_connection() as conn:
            cur = conn.execute("SELECT * FROM tasks ORDER BY id")
            return cur.fetchall()

    def mark_done(self, task_id):
        with get_connection() as conn:
            conn.execute("UPDATE tasks SET status='done' "
                         "WHERE id=?", (task_id,))

    def delete(self, task_id):
        with get_connection() as conn:
            conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
            conn.commit()

    def search(self, task=None, task_id=None):
        pass

    def update(self, task_id, title=None, desc=None, due=None, tag=None):
        updates = []
        params = []
        pass