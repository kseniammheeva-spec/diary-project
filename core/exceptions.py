"""Кастомные исключения."""


class DiaryError(Exception):
    """Базовое исключение приложения."""


class NotFoundError(DiaryError):
    """Объект не найден."""
