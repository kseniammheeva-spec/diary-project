"""Модель оценки."""


class Grade:
    """Оценка ученика по предмету."""

    def __init__(self, grade_id: int, student_id: int, subject: str, value: int, date: str):
        self.grade_id = grade_id
        self.student_id = student_id
        self.subject = subject
        self.value = value
        self.date = date

    def __repr__(self):
        return f"Grade(id={self.grade_id!r}, student_id={self.student_id!r}, value={self.value!r})"

    def __eq__(self, other):
        return isinstance(other, Grade) and self.grade_id == other.grade_id

    def __hash__(self):
        return hash(self.grade_id)