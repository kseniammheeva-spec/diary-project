"""Сервис оценок."""


class GradeService:
    """Бизнес-логика работы с оценками."""

    def __init__(self, repo):
        self.repo = repo

    def calculate_average(self, student_id: int):
        # TODO: получить оценки и посчитать средний балл
        raise NotImplementedError