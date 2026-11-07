"""Модель ученика."""


class Student:
    """Ученик школы."""

    def __init__(self, student_id: int, full_name: str, class_name: str):
        self.student_id = student_id
        self.full_name = full_name
        self.class_name = class_name

    def __repr__(self):
        return f"Student(id={self.student_id!r}, name={self.full_name!r})"
