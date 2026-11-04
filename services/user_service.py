"""Сервис пользователей."""


class UserService:
    """Бизнес-логика работы с пользователями."""

    def __init__(self, repo):
        self.repo = repo

    def get_student(self, user_id: int):
        # TODO: валидация роли + вызов repo
        raise NotImplementedError