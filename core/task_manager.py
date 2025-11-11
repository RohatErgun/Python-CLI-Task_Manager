from core.database import get_connection


def add(title, description="", due_date=None, tag=None):
    with get_connection() as conn:
        conn.execute("INSERT INTO tasks (title, description, due_date, tag) "
                     "VALUES (?, ?, ?, ?)",
                     (title, description, due_date, tag))
        conn.commit()


def list_tasks():
    with get_connection() as conn:
        cur = conn.execute("SELECT * FROM tasks "
                           "ORDER BY id")
        for row in cur.fetchall():
            print(f"[{row['id']}] {row['title']} ({row['status']})")


def mark_complete(task_id):
    with get_connection() as conn:
        conn.execute("UPDATE tasks SET status='done' "
                     "WHERE id=?", (task_id,))
        conn.commit()


def delete(task_id):
    with get_connection() as conn:
        cur = conn.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
        task = cur.fetchall()

        if task:
            conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
            conn.commit()
            print(f"Task:{task_id} has been deleted")
        else:
            print(f"Task:{task_id} not found")


""" Not implemented : Checking the need """


def info(task_id):
    with get_connection() as conn:
        cur = conn.execute(
            "SELECT title, description, due_date, tag from tasks"
            "where id=?", (task_id,)
        )
        for row in cur.fetchall():
            print(f"<{row['title']} {row['description']} {row['due_date']} {row['tag']} {row['status']}>")
