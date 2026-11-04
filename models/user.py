"""Модель пользователя (ученик/учитель/родитель)."""


class User:
    """Пользователь системы."""

    def __init__(self, user_id: int, full_name: str, role: str):
        self.user_id = user_id
        self.full_name = full_name
        self.role = role

    def __repr__(self):
        return f"User(id={self.user_id!r}, role={self.role!r})"

    def __eq__(self, other):
        return isinstance(other, User) and self.user_id == other.user_id

    def __hash__(self):
        return hash(self.user_id)