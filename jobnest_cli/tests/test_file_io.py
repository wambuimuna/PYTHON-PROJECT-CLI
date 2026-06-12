from models.user import User


def test_user_to_from_dict():
    u = User(user_id="u1", name="Alice", email="a@example.com")
    d = u.to_dict()
    u2 = User.from_dict(d)
    assert u2.id == "u1"
    assert u2.email == "a@example.com"
