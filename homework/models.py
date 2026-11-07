"""Модель домашнего задания."""


class Homework:
    def __init__(self, hw_id: int, description: str):
        self.hw_id = hw_id
        self.description = description
