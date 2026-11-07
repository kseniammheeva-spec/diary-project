"""Модуль расписания."""
from schedule.models import Lesson
from schedule.service import ScheduleService

__all__ = ["Lesson", "ScheduleService"]