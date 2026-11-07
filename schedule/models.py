"""Модель урока."""

class Lesson:
    def __init__(self, lesson_id: int, subject: str):
        self.lesson_id = lesson_id
        self.subject = subject