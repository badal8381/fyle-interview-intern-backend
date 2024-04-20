from core.models.users import User

def test_user_model():
    user = User()
    user.username = 'testuser'
    user.email = 'test@gmail.com'

    assert str(user) == "<User 'testuser'>"
