"""Сервис оценок."""


class GradeService:
    """Бизнес-логика работы с оценками."""

    def __init__(self, repo):
        self.repo = repo

    def calculate_average(self, student_id: int):
        # TODO: получить оценки и посчитать средний балл
        grades = []  # В будущем здесь будет вызов self.repo.get_by_student(student_id)
        if not grades:
            return 0  # Возвращаем 0, если оценок нет (чтобы не было деления на ноль)
        
        # TODO: реализовать подсчет среднего
        raise NotImplementedError