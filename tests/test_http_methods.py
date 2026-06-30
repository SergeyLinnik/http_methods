# -*- coding: utf-8 -*-
"""
Тесты для HTTP методов.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from http_methods import HTTPMethods


def test_get_method() -> None:
    """Тест GET запроса."""
    print("\n🔍 Тест GET метода...")
    url = "https://api.chucknorris.io/jokes/random"
    response = HTTPMethods.get(url)
    print(f"   URL: {url}")
    print(f"   Статус-код: {response.status_code}")
    assert response.status_code == 200, f"GET вернул {response.status_code}"
    print("   ✅ GET запрос выполнен успешно!")


def test_post_method() -> None:
    """Тест POST запроса."""
    print("\n📮 Тест POST метода...")
    url = "https://jsonplaceholder.typicode.com/posts"
    body = {"title": "Test post", "body": "This is a test post", "userId": 1}
    response = HTTPMethods.post(url, body)
    print(f"   URL: {url}")
    print(f"   Body: {body}")
    print(f"   Статус-код: {response.status_code}")
    assert response.status_code == 201, f"POST вернул {response.status_code}"
    print("   ✅ POST запрос выполнен успешно!")


def test_put_method() -> None:
    """Тест PUT запроса."""
    print("\n📝 Тест PUT метода...")
    url = "https://jsonplaceholder.typicode.com/posts/1"
    body = {"id": 1, "title": "Updated title", "body": "Updated body", "userId": 1}
    response = HTTPMethods.put(url, body)
    print(f"   URL: {url}")
    print(f"   Body: {body}")
    print(f"   Статус-код: {response.status_code}")
    assert response.status_code == 200, f"PUT вернул {response.status_code}"
    print("   ✅ PUT запрос выполнен успешно!")


def test_delete_method() -> None:
    """Тест DELETE запроса."""
    print("\n🗑️ Тест DELETE метода...")
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = HTTPMethods.delete(url)
    print(f"   URL: {url}")
    print(f"   Статус-код: {response.status_code}")
    assert response.status_code in [200, 204], f"DELETE вернул {response.status_code}"
    print("   ✅ DELETE запрос выполнен успешно!")


if __name__ == "__main__":
    test_get_method()
    test_post_method()
    test_put_method()
    test_delete_method()