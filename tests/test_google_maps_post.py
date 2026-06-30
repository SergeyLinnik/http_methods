# -*- coding: utf-8 -*-
"""
Тест POST метода Google Maps API.
Проверяет создание нового места.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google_maps_api import GoogleMapsAPI


def test_create_place() -> None:
    """
    Тест создания места через POST запрос.
    Проверяет:
    1. Статус-код ответа
    2. Наличие place_id в ответе
    3. Статус "OK" в ответе
    """
    print("\n" + "="*60)
    print(" ТЕСТ: POST ЗАПРОС (СОЗДАНИЕ МЕСТА)")
    print("="*60)

    # --------------------------------------------------------------------
    # ШАГ 1: Создание места через POST
    # --------------------------------------------------------------------
    print("\n[ШАГ 1] Отправка POST запроса на создание места...")

    response = GoogleMapsAPI.create_place()

    # --------------------------------------------------------------------
    # ШАГ 2: Проверка ответа
    # --------------------------------------------------------------------
    print("\n[ШАГ 2] Проверка ответа API...")

    assert response.get("status") == "OK", \
        f"Статус ответа не 'OK': {response.get('status')}"

    place_id = response.get("place_id")
    assert place_id is not None, "place_id отсутствует в ответе"
    print(f"   ✅ place_id получен: {place_id}")

    assert response.get("scope") == "APP", \
        f"scope не 'APP': {response.get('scope')}"

    print(f"   ✅ scope: {response.get('scope')}")

    # --------------------------------------------------------------------
    # ШАГ 3: Вывод результата
    # --------------------------------------------------------------------
    print("\n" + "="*60)
    print(" РЕЗУЛЬТАТ ТЕСТА")
    print("="*60)

    print(f"\n📊 СТАТИСТИКА:")
    print(f"   Статус ответа: {response.get('status')}")
    print(f"   place_id: {place_id}")
    print(f"   scope: {response.get('scope')}")
    print(f"   reference: {response.get('reference')}")

    print("\n" + "="*60)
    print("✅ ТЕСТ POST ПРОЙДЕН УСПЕШНО!")
    print("="*60)


if __name__ == "__main__":
    test_create_place()