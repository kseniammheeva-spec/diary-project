"""Модуль домашних заданий."""

from homework.models import Homework
from homework.service import HomeworkService

__all__ = ["Homework", "HomeworkService"]
