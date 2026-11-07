"""Модуль работы с учениками."""

from students.models import Student
from students.service import StudentService

__all__ = ["Student", "StudentService"]
