"""Контракты между модулями."""
from typing import Protocol


class StudentRepository(Protocol):
    """Контракт репозитория учеников."""

    def get_by_id(self, student_id: int): ...
    def list_all(self): ...


class GradeRepository(Protocol):
    """Контракт репозитория оценок."""

    def get_by_student(self, student_id: int): ...
    def add(self, grade): ...