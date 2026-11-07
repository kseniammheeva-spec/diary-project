"""Репозиторий учеников."""


class StudentRepository:
    """Доступ к данным учеников."""

    def __init__(self, conn):
        self.conn = conn

    def get_by_id(self, student_id: int):
        # TODO: реализовать запрос
        raise NotImplementedError
