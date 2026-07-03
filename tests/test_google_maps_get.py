# -*- coding: utf-8 -*-
"""
Тест GET метода Google Maps API.
Проверяет получение данных о месте по place_id.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google_maps_api import GoogleMapsAPI


def test_get_place() -> None:
    """
    Тест получения данных о месте через GET запрос.
    Проверяет:
    1. Статус-код ответа
    2. Наличие данных о месте
    3. Корректность полученных данных
    """
    print("\n" + "="*60)
    print(" ТЕСТ: GET ЗАПРОС (ПОЛУЧЕНИЕ ДАННЫХ О МЕСТЕ)")
    print("="*60)

    # --------------------------------------------------------------------
    # ШАГ 1: Создание места через POST (для получения place_id)
    # --------------------------------------------------------------------
    print("\n[ШАГ 1] Создание места через POST...")

    create_response = GoogleMapsAPI.create_place()
    place_id: str = create_response.get("place_id")

    print(f"   ✅ Место создано, place_id: {place_id}")

    # --------------------------------------------------------------------
    # ШАГ 2: Получение данных о месте через GET
    # --------------------------------------------------------------------
    print("\n[ШАГ 2] Получение данных о месте через GET...")

    get_response = GoogleMapsAPI.get_place(place_id)

    # --------------------------------------------------------------------
    # ШАГ 3: Проверка полученных данных
    # --------------------------------------------------------------------
    print("\n[ШАГ 3] Проверка полученных данных...")

    # Проверка названия
    expected_name: str = "Frontline house"
    actual_name: str = get_response.get("name", "")
    assert actual_name == expected_name, \
        f"Ожидалось название '{expected_name}', получено '{actual_name}'"
    print(f"   ✅ Название: {actual_name}")

    # Проверка адреса
    expected_address: str = "29, side layout, cohen 09"
    actual_address: str = get_response.get("address", "")
    assert actual_address == expected_address, \
        f"Ожидался адрес '{expected_address}', получен '{actual_address}'"
    print(f"   ✅ Адрес: {actual_address}")

    # Проверка телефона
    expected_phone: str = "(+91) 983 893 3937"
    actual_phone: str = get_response.get("phone_number", "")
    assert actual_phone == expected_phone, \
        f"Ожидался телефон '{expected_phone}', получен '{actual_phone}'"
    print(f"   ✅ Телефон: {actual_phone}")

    # Проверка location
    location = get_response.get("location", {})
    assert location.get("latitude") == "-38.383494", \
        f"Ожидалась широта '-38.383494', получена '{location.get('latitude')}'"
    assert location.get("longitude") == "33.427362", \
        f"Ожидалась долгота '33.427362', получена '{location.get('longitude')}'"
    print(f"   ✅ Локация: широта {location.get('latitude')}, долгота {location.get('longitude')}")

    # --------------------------------------------------------------------
    # ШАГ 4: Вывод результата
    # --------------------------------------------------------------------
    print("\n" + "="*60)
    print(" РЕЗУЛЬТАТ ТЕСТА")
    print("="*60)

    print(f"\n📊 ДАННЫЕ О МЕСТЕ:")
    print(f"   Название: {get_response.get('name')}")
    print(f"   Адрес: {get_response.get('address')}")
    print(f"   Телефон: {get_response.get('phone_number')}")
    print(f"   Типы: {get_response.get('types')}")
    print(f"   Язык: {get_response.get('language')}")

    print("\n" + "="*60)
    print("✅ ТЕСТ GET ПРОЙДЕН УСПЕШНО!")
    print("="*60)


if __name__ == "__main__":
    test_get_place()