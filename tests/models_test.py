from core.models.teachers import Teacher

def test_teacher_model():
    id = 1
    teacher = Teacher()
    teacher.id = id
    teacher.username = 'testteacher'

    assert str(teacher) == f"<Teacher {id}>"
    assert teacher.id == id