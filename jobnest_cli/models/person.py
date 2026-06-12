class Person:

    _id_counter = 0

    def __init__(self, name, email):
        Person._id_counter += 1
        self.id = Person._id_counter
        self.name = name
        self.email = email

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}

    @classmethod
    def from_dict(cls, data):
        p = cls(data.get("name", ""), data.get("email", ""))
        p.id = data.get("id", p.id)
        return p

    def __str__(self):
        return f"{self.name} - {self.email}"