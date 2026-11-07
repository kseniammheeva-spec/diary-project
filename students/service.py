"""Сервис учеников."""


class StudentService:
    """Бизнес-логика учеников."""

    def __init__(self, repo):
        self.repo = repo

    def get_student(self, student_id: int):
        # TODO: валидация + вызов repo
        raise NotImplementedError