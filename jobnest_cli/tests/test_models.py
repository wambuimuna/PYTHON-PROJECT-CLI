import pytest
from jobnest_cli.models.user import User
from jobnest_cli.models.project import Project
from jobnest_cli.models.task import Task

def test_user_creation():
    u = User("Alex", "alex@test.com", ["Python", "Django"])
    assert u.name == "Alex"
    assert "Python" in u.skills

def test_add_project_to_user():
    u = User("Sam", "sam@test.com")
    p = Project("Build API", due_date="2025-12-01")
    u.add_project(p)
    assert len(u.projects) == 1
    assert u.projects[0].title == "Build API"

def test_task_completion():
    t = Task("Write tests")
    assert t.status == "pending"
    t.complete()
    assert t.status == "done"

def test_user_serialization():
    u = User("Jo", "jo@test.com", ["React"])
    u.add_project(Project("Portfolio site"))
    d = u.to_dict()
    restored = User.from_dict(d)
    assert restored.name == "Jo"
    assert restored.projects[0].title == "Portfolio site"