"""Тесты для модуля students."""


def test_student_placeholder():
    """Заглушка: модуль импортируется."""
    from students import Student

    student = Student(1, "Иванов Иван", "7А")
    assert student.student_id == 1
