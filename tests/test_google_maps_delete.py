# -*- coding: utf-8 -*-
"""
Тест DELETE метода Google Maps API.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import GoogleMapsAPI
from utils import TestHelpers


def test_delete_place() -> None:
    """Тест удаления места через DELETE."""
    print("\n" + "="*60)
    print(" ТЕСТ: DELETE ЗАПРОС (УДАЛЕНИЕ МЕСТА)")
    print("="*60)

    print("\n[ШАГ 1] Создание места через POST...")
    create_response, _ = GoogleMapsAPI.create_place()
    place_id = create_response.get("place_id")
    print(f"   ✅ Место создано, place_id: {place_id}")

    print("\n[ШАГ 2] Удаление места через DELETE...")
    delete_response, delete_resp = GoogleMapsAPI.delete_place(place_id)

    print("\n[ШАГ 3] Проверка статус-кода...")
    TestHelpers.check_status_code(delete_resp, 200)

    print("\n[ШАГ 4] Проверка обязательных полей...")
    required_fields = ["status"]
    TestHelpers.check_required_fields(delete_response, required_fields)

    print("\n[ШАГ 5] Проверка содержимого полей...")
    TestHelpers.check_field_value(delete_response, "status", "OK", "статус удаления")

    print("\n[ШАГ 6] Проверка через GET что место удалено...")
    try:
        GoogleMapsAPI.get_place(place_id)
        assert False, "Место все еще существует!"
    except AssertionError:
        print("   ✅ Место успешно удалено (GET не находит место)")

    print("\n" + "="*60)
    print("✅ ТЕСТ DELETE ПРОЙДЕН УСПЕШНО!")
    print("="*60)


if __name__ == "__main__":
    test_delete_place()