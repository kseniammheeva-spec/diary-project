"""Репозиторий пользователей."""


class UserRepository:
    """Доступ к данным пользователей."""

    def __init__(self, conn):
        self.conn = conn

    def get_by_id(self, user_id: int):
        # TODO: реализовать запрос к БД
        raise NotImplementedError

    def list_students(self):
        # TODO: реализовать выборку учеников
        raise NotImplementedError