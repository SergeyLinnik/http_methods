# -*- coding: utf-8 -*-
"""
Тест PUT метода Google Maps API.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import GoogleMapsAPI
from utils import TestHelpers


def test_update_place() -> None:
    """Тест обновления адреса места через PUT."""
    print("\n" + "="*60)
    print(" ТЕСТ: PUT ЗАПРОС (ОБНОВЛЕНИЕ АДРЕСА)")
    print("="*60)

    # --------------------------------------------------------------------
    # ШАГ 1: Создание места через POST
    # --------------------------------------------------------------------
    print("\n[ШАГ 1] Создание места через POST...")

    create_response, _ = GoogleMapsAPI.create_place()  # Распаковка кортежа
    place_id = create_response.get("place_id")
    print(f"   ✅ Место создано, place_id: {place_id}")

    # --------------------------------------------------------------------
    # ШАГ 2: Обновление адреса через PUT
    # --------------------------------------------------------------------
    new_address = "100 Lenina street, RU"
    print(f"\n[ШАГ 2] Обновление адреса через PUT...")
    print(f"   Новый адрес: {new_address}")

    put_response, put_resp = GoogleMapsAPI.update_place(place_id, new_address)

    # --------------------------------------------------------------------
    # ШАГ 3: Проверка статус-кода
    # --------------------------------------------------------------------
    print("\n[ШАГ 3] Проверка статус-кода...")
    TestHelpers.check_status_code(put_resp, 200)

    # --------------------------------------------------------------------
    # ШАГ 4: Проверка обязательных полей
    # --------------------------------------------------------------------
    print("\n[ШАГ 4] Проверка обязательных полей...")
    required_fields = ["msg"]
    TestHelpers.check_required_fields(put_response, required_fields)

    # --------------------------------------------------------------------
    # ШАГ 5: Проверка содержимого
    # --------------------------------------------------------------------
    print("\n[ШАГ 5] Проверка содержимого...")
    assert "updated" in put_response.get("msg").lower()
    print(f"   ✅ Сообщение: {put_response.get('msg')}")

    # --------------------------------------------------------------------
    # ШАГ 6: Проверка через GET
    # --------------------------------------------------------------------
    print("\n[ШАГ 6] Проверка через GET что адрес обновлен...")
    get_response, _ = GoogleMapsAPI.get_place(place_id)
    assert get_response.get("address") == new_address
    print(f"   ✅ Адрес обновлен: {get_response.get('address')}")

    print("\n" + "="*60)
    print("✅ ТЕСТ PUT ПРОЙДЕН УСПЕШНО!")
    print("="*60)


if __name__ == "__main__":
    test_update_place()