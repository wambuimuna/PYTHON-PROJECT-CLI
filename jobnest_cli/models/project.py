class Project:

    _id_counter = 0

    def __init__(self, title, description="", due_date=""):
        Project._id_counter += 1
        self.id = Project._id_counter
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "description": self.description, "due_date": self.due_date, "tasks": [t.to_dict() for t in self.tasks]}

    @classmethod
    def from_dict(cls, data):
        from jobnest_cli.models.task import Task
        p = cls(data.get("title", "Untitled"), data.get("description", ""), data.get("due_date", ""))
        p.id = data.get("id", p.id)
        p.tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
        return p

    def tasks_status(self):
        total = len(self.tasks)
        done = len([t for t in self.tasks if t.status == "done"]) if total else 0
        return done, total

    def __str__(self):
        done, total = self.tasks_status()
        tasks_part = f"{done}/{total}" if total else "no tasks"
        due = self.due_date or "(no due)"
        return f"{self.title} - due {due} - {tasks_part}"