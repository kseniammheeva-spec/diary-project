# Перечень артефактов проекта «Электронный дневник»

## Матрица артефактов

| ID | Артефакт | Тип | Этап | Владелец | Место хранения | Формат | Версия | Статус | Критерии готовности |
|---|---|---|---|---|---|---|---|---|---|
| A-01 | ТЗ | Документ | Анализ | Аналитик | Git `docs/tz.md` | Markdown | v1.0 | Готов | Согласовано, 8 разделов |
| A-02 | IDEF0 A-0 | Модель | Анализ | Аналитик | Git `docs/idef0.png` | PNG | v1.0 | Готов | Стрелки подписаны |
| A-03 | IDEF1X | Модель | Анализ | Аналитик | Git `docs/idef1x.png` | PNG | v1.0 | Готов | 5 сущностей, связи |
| A-04 | Архитектура | Документ | Проектирование | Архитектор | Git `docs/architecture.md` | Markdown | v1.0 | Готов | 4 слоя, ADR ≥ 3 |
| A-05 | UML Component | Модель | Проектирование | Архитектор | Git `docs/components.puml` | PlantUML | v1.0 | Готов | Без циклов |
| A-06 | Схема БД | Данные | Проектирование | Архитектор | Git `docs/schema.sql` | SQL | v1.0 | Готов | PK/FK, 5 таблиц |
| A-07 | Код `students` | Код | Разработка | Разработчик | Git `students/` | Python | main | В работе | Модуль + тесты |
| A-08 | Код `grades` | Код | Разработка | Разработчик | Git `grades/` | Python | main | В работе | Модуль + тесты |
| A-09 | Код `homework` | Код | Разработка | Разработчик | Git `homework/` | Python | main | В работе | Модуль + тесты |
| A-10 | Код `schedule` | Код | Разработка | Разработчик | Git `schedule/` | Python | main | В работе | Модуль + тесты |
| A-11 | Модульные тесты | Тесты | Разработка | Тестировщик | Git `*/tests/` | Python | main | В работе | Покрытие ≥ 70% |
| A-12 | Интеграционные тесты | Тесты | Тестирование | Тестировщик | Git `tests/` | Python | main | План | Покрытие ≥ 70% |
| A-13 | pyproject.toml | Конфигурация | Разработка | DevOps | Git `pyproject.toml` | TOML | main | Готов | black, ruff, pytest |
| A-14 | .gitignore | Конфигурация | Разработка | DevOps | Git `.gitignore` | Text | main | Готов | Python + IDE + БД |
| A-15 | CI workflow | Конфигурация | Разработка | DevOps | Git `.github/workflows/ci.yml` | YAML | main | План | pytest + coverage |
| A-16 | README | Документ | Все этапы | Разработчик | Git `README.md` | Markdown | main | Готов | Установка, запуск, тесты |
| A-17 | CHANGELOG | Документ | Внедрение | DevOps | Git `CHANGELOG.md` | Markdown | main | План | v0.1.0 |
| A-18 | Релиз v0.1.0 | Релиз | Внедрение | DevOps | GitHub Releases | Tag + wheel | v0.1.0 | План | Тег, описание |

## Трассировка артефактов к требованиям

| Артефакт | FR/NFR |
|---|---|
| `students/service.py` | FR-07 Управление пользователями |
| `grades/service.py` | FR-02 Выставление оценки |
| `homework/service.py` | FR-03 Задание ДЗ |
| `schedule/service.py` | FR-07 Управление расписанием |
| `students/tests/` | FR-07 |
| `grades/tests/` | FR-02 |
| `docs/architecture.md` | NFR-01, NFR-02 |
| `README.md` | — (общий) |

## Артефакты CI/CD

| Артефакт CI/CD | Что создаётся |
|---|---|
| Отчёт pytest | JUnit XML |
| Отчёт покрытия | coverage.xml, HTML |
| Отчёт линтеров | ruff output |
| Wheel-пакет | diary-0.1.0-py3-none-any.whl |
| Docker-образ | diary:0.1.0 |

## Артефакты релиза v0.1.0

- тег `v0.1.0`;
- wheel-пакет;
- Docker-образ;
- CHANGELOG;
- README;
- исходный код (zip).
