"""Базовый тест работоспособности приложения."""


def test_index_returns_200(client):
    """GET / возвращает 200 и текст приветствия."""
    response = client.get("/")
    assert response.status_code == 200
    assert "Электронный дневник" in response.text
