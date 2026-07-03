# -*- coding: utf-8 -*-
"""
Тест проверки статус-кода.
Использует метод check_status_code из HTTPMethods.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from http_methods import HTTPMethods


def test_status_code_check() -> None:
    """
    Тест проверки статус-кода.
    Отправляет GET запрос и проверяет статус-код через специальный метод.
    """
    print("\n" + "="*60)
    print(" ТЕСТ: ПРОВЕРКА СТАТУС-КОДА")
    print("="*60)

    # --------------------------------------------------------------------
    # ШАГ 1: Отправка GET запроса
    # --------------------------------------------------------------------
    print("\n[ШАГ 1] Отправка GET запроса...")

    url: str = "https://api.chucknorris.io/jokes/random"
    response = HTTPMethods.get(url)

    print(f"   URL: {url}")
    print(f"   Статус-код: {response.status_code}")

    # --------------------------------------------------------------------
    # ШАГ 2: Проверка статус-кода через метод check_status_code
    # --------------------------------------------------------------------
    print("\n[ШАГ 2] Проверка статус-кода через метод check_status_code...")

    expected_status: int = 200
    status_ok = HTTPMethods.check_status_code(response, expected_status)

    # --------------------------------------------------------------------
    # ШАГ 3: Дополнительные проверки
    # --------------------------------------------------------------------
    print("\n[ШАГ 3] Дополнительная проверка статус-кода...")

    # Проверка с неверным статусом (должна вызвать AssertionError)
    # HTTPMethods.check_status_code(response, 404)  # Раскомментировать для проверки ошибки

    # --------------------------------------------------------------------
    # ШАГ 4: Вывод результата
    # --------------------------------------------------------------------
    print("\n" + "="*60)
    print(" РЕЗУЛЬТАТ ТЕСТА")
    print("="*60)

    print(f"\n📊 СТАТИСТИКА:")
    print(f"   URL: {url}")
    print(f"   Статус-код: {response.status_code}")
    print(f"   Ожидаемый статус: {expected_status}")
    print(f"   ✅ Проверка статус-кода успешна!")

    print("\n" + "="*60)
    print("✅ ТЕСТ СТАТУС-КОДА ПРОЙДЕН УСПЕШНО!")
    print("="*60)


if __name__ == "__main__":
    test_status_code_check()