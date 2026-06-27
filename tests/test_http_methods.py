# -*- coding: utf-8 -*-
"""
Тесты для HTTP методов.
Проверяет работу GET, POST, PUT, DELETE запросов.
"""

import pytest
import sys
import os

# Добавляем путь к корню проекта
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from http_methods import HTTP_methods


class TestHTTPMethods:
    """
    Тестовый класс для проверки HTTP методов.
    Использует публичное API для демонстрации.
    """

    # ------------------------------------------------------------------------
    # ТЕСТ GET МЕТОДА
    # ------------------------------------------------------------------------

    def test_get_method(self) -> None:
        """
        Тест GET запроса.
        Отправляет GET запрос и проверяет статус-код.
        """
        print("\n🔍 Тест GET метода...")

        url: str = "https://api.chucknorris.io/jokes/random"
        response = HTTP_methods.get(url)

        print(f"   URL: {url}")
        print(f"   Статус-код: {response.status_code}")

        assert response.status_code == 200, \
            f"GET запрос вернул статус {response.status_code}"
        print(f"   ✅ GET запрос выполнен успешно!")

    # ------------------------------------------------------------------------
    # ТЕСТ POST МЕТОДА
    # ------------------------------------------------------------------------

    def test_post_method(self) -> None:
        """
        Тест POST запроса.
        Отправляет POST запрос и проверяет статус-код.
        """
        print("\n📮 Тест POST метода...")

        url: str = "https://jsonplaceholder.typicode.com/posts"
        body: dict = {
            "title": "Test post",
            "body": "This is a test post",
            "userId": 1
        }

        response = HTTP_methods.post(url, body)

        print(f"   URL: {url}")
        print(f"   Body: {body}")
        print(f"   Статус-код: {response.status_code}")

        assert response.status_code == 201, \
            f"POST запрос вернул статус {response.status_code}"
        print(f"   ✅ POST запрос выполнен успешно!")

    # ------------------------------------------------------------------------
    # ТЕСТ PUT МЕТОДА
    # ------------------------------------------------------------------------

    def test_put_method(self) -> None:
        """
        Тест PUT запроса.
        Отправляет PUT запрос и проверяет статус-код.
        """
        print("\n📝 Тест PUT метода...")

        url: str = "https://jsonplaceholder.typicode.com/posts/1"
        body: dict = {
            "id": 1,
            "title": "Updated title",
            "body": "Updated body",
            "userId": 1
        }

        response = HTTP_methods.put(url, body)

        print(f"   URL: {url}")
        print(f"   Body: {body}")
        print(f"   Статус-код: {response.status_code}")

        assert response.status_code == 200, \
            f"PUT запрос вернул статус {response.status_code}"
        print(f"   ✅ PUT запрос выполнен успешно!")

    # ------------------------------------------------------------------------
    # ТЕСТ DELETE МЕТОДА
    # ------------------------------------------------------------------------

    def test_delete_method(self) -> None:
        """
        Тест DELETE запроса.
        Отправляет DELETE запрос и проверяет статус-код.
        """
        print("\n🗑️ Тест DELETE метода...")

        url: str = "https://jsonplaceholder.typicode.com/posts/1"

        response = HTTP_methods.delete(url)

        print(f"   URL: {url}")
        print(f"   Статус-код: {response.status_code}")

        # JSONPlaceholder возвращает 200 для DELETE
        assert response.status_code in [200, 204], \
            f"DELETE запрос вернул статус {response.status_code}"
        print(f"   ✅ DELETE запрос выполнен успешно!")


# ============================================================================
# ЗАПУСК ТЕСТОВ
# ============================================================================

if __name__ == "__main__":
    test = TestHTTPMethods()
    test.test_get_method()
    test.test_post_method()
    test.test_put_method()
    test.test_delete_method()