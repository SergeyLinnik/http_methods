# -*- coding: utf-8 -*-
"""
Тест GET метода Google Maps API.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import GoogleMapsAPI
from utils import TestHelpers


def test_get_place() -> None:
    """Тест получения данных о месте через GET."""
    print("\n" + "="*60)
    print(" ТЕСТ: GET ЗАПРОС (ПОЛУЧЕНИЕ ДАННЫХ О МЕСТЕ)")
    print("="*60)

    print("\n[ШАГ 1] Создание места через POST...")
    create_response, _ = GoogleMapsAPI.create_place()
    place_id = create_response.get("place_id")
    print(f"   ✅ Место создано, place_id: {place_id}")

    print("\n[ШАГ 2] Получение данных о месте через GET...")
    get_response, get_resp = GoogleMapsAPI.get_place(place_id)

    print("\n[ШАГ 3] Проверка статус-кода...")
    TestHelpers.check_status_code(get_resp, 200)

    print("\n[ШАГ 4] Проверка обязательных полей...")
    required_fields = ["location", "name", "address", "phone_number", "types"]
    TestHelpers.check_required_fields(get_response, required_fields)

    print("\n[ШАГ 5] Проверка содержимого полей...")
    TestHelpers.check_field_value(get_response, "name", "Frontline house", "название")
    TestHelpers.check_field_value(get_response, "address", "29, side layout, cohen 09", "адрес")
    TestHelpers.check_field_value(get_response, "phone_number", "(+91) 983 893 3937", "телефон")

    print("\n" + "="*60)
    print("✅ ТЕСТ GET ПРОЙДЕН УСПЕШНО!")
    print("="*60)


if __name__ == "__main__":
    test_get_place()