# -*- coding: utf-8 -*-
"""
Тест POST метода Google Maps API.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import GoogleMapsAPI
from utils import TestHelpers


def test_create_place() -> None:
    """Тест создания места через POST."""
    print("\n" + "="*60)
    print(" ТЕСТ: POST ЗАПРОС (СОЗДАНИЕ МЕСТА)")
    print("="*60)

    print("\n[ШАГ 1] Отправка POST запроса...")
    response_json, response = GoogleMapsAPI.create_place()

    print("\n[ШАГ 2] Проверка статус-кода...")
    TestHelpers.check_status_code(response, 200)

    print("\n[ШАГ 3] Проверка обязательных полей...")
    required_fields = ["status", "place_id", "scope", "reference", "id"]
    TestHelpers.check_required_fields(response_json, required_fields)

    print("\n[ШАГ 4] Проверка содержимого...")
    assert response_json.get("status") == "OK"
    assert response_json.get("place_id") is not None
    assert response_json.get("scope") == "APP"

    print("\n" + "="*60)
    print("✅ ТЕСТ POST ПРОЙДЕН УСПЕШНО!")
    print("="*60)


if __name__ == "__main__":
    test_create_place()