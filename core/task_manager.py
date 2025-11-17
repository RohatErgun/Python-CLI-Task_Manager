from core.database import get_connection


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

    def search(self, title=None, task_id=None, tag=None):
        with get_connection() as conn:
            query = "SELECT * FROM tasks WHERE 1=1"
            params = []

            if title is not None:
                query += " AND title LIKE ?"
                params.append(f"%{title}%")

            if task_id is not None:
                query += " AND id = ?"
                params.append(task_id)

            if tag is not None:
                query += " AND tag = ?"
                params.append(tag)

            cursor = conn.execute(query, params)
            return cursor.fetchall()


    def update(self, task_id, title=None, desc=None, due=None, tag=None):
        updates = []
        params = []
        pass