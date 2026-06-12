from jobnest_cli.models.person import Person

class User(Person):
    _id_counter = 0  

    def __init__(self, name, email, skills=None, bio="", user_id=None):
        super().__init__(name, email)
        
        if user_id is None:
            User._id_counter += 1
            self.id = User._id_counter
        else:
            self.id = user_id
            
        self.skills = skills if skills is not None else []
        self.bio = bio
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "skills": self.skills,
            "bio": self.bio,
            "projects": [p.to_dict() for p in self.projects]
        }

    @classmethod
    def from_dict(cls, data):
        from jobnest_cli.models.project import Project
        user = cls(
            name=data["name"],
            email=data["email"],
            skills=data.get("skills", []),
            bio=data.get("bio", ""),
            user_id=data.get("id")
        )
        user.projects = [Project.from_dict(p) for p in data.get("projects", [])]
        return user