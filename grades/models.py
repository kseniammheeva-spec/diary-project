"""Модель оценки."""


class Grade:
    """Оценка ученика."""

    def __init__(self, grade_id: int, student_id: int, value: int):
        self.grade_id = grade_id
        self.student_id = student_id
        self.value = value
