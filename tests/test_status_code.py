# -*- coding: utf-8 -*-
"""
Тест проверки статус-кода.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.http_methods import HTTPMethods
from utils.test_helpers import TestHelpers


def test_status_code_check() -> None:
    """Тест проверки статус-кода."""
    print("\n" + "="*60)
    print(" ТЕСТ: ПРОВЕРКА СТАТУС-КОДА")
    print("="*60)

    print("\n[ШАГ 1] Отправка GET запроса...")
    url = "https://api.chucknorris.io/jokes/random"
    response = HTTPMethods.get(url)
    print(f"   URL: {url}")
    print(f"   Статус-код: {response.status_code}")

    print("\n[ШАГ 2] Проверка статус-кода...")
    TestHelpers.check_status_code(response, 200)

    print("\n" + "="*60)
    print("✅ ТЕСТ СТАТУС-КОДА ПРОЙДЕН УСПЕШНО!")
    print("="*60)


if __name__ == "__main__":
    test_status_code_check()