class Task:

    _id_counter = 0

    def __init__(self, title, assigned_to="", status="pending"):
        Task._id_counter += 1
        self.id = Task._id_counter
        self.title = title
        self.assigned_to = assigned_to
        self.status = status

    def complete(self):
        self.status = "done"

    def to_dict(self):
        return {"id": self.id, "title": self.title, "assigned_to": self.assigned_to, "status": self.status}

    @classmethod
    def from_dict(cls, data):
        t = cls(data.get("title", ""), data.get("assigned_to", ""), data.get("status", "pending"))
        t.id = data.get("id", t.id)
        return t

    def __str__(self):
        a = self.assigned_to or "(unassigned)"
        return f"{self.id}. {self.title} - {a} [{self.status}]"
