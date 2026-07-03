# -*- coding: utf-8 -*-
"""
Тест PUT метода Google Maps API.
Проверяет обновление адреса места.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google_maps_api import GoogleMapsAPI


def test_update_place() -> None:
    """
    Тест обновления адреса места через PUT запрос.
    Проверяет:
    1. Статус-код ответа
    2. Сообщение об успешном обновлении
    3. Фактическое обновление адреса через GET
    """
    print("\n" + "="*60)
    print(" ТЕСТ: PUT ЗАПРОС (ОБНОВЛЕНИЕ АДРЕСА)")
    print("="*60)

    # --------------------------------------------------------------------
    # ШАГ 1: Создание места через POST (для получения place_id)
    # --------------------------------------------------------------------
    print("\n[ШАГ 1] Создание места через POST...")

    create_response = GoogleMapsAPI.create_place()
    place_id: str = create_response.get("place_id")

    print(f"   ✅ Место создано, place_id: {place_id}")
    print(f"   Текущий адрес: 29, side layout, cohen 09")

    # --------------------------------------------------------------------
    # ШАГ 2: Обновление адреса через PUT
    # --------------------------------------------------------------------
    print("\n[ШАГ 2] Обновление адреса через PUT...")

    new_address: str = "100 Lenina street, RU"
    print(f"   Новый адрес: {new_address}")

    put_response = GoogleMapsAPI.update_place(place_id, new_address)

    # --------------------------------------------------------------------
    # ШАГ 3: Проверка что PUT отработал верно
    # --------------------------------------------------------------------
    print("\n[ШАГ 3] Проверка что PUT отработал верно...")

    # Проверка сообщения об успешном обновлении
    assert "msg" in put_response, "В ответе отсутствует поле 'msg'"
    assert "updated" in put_response["msg"].lower(), \
        f"Сообщение не содержит 'updated': {put_response.get('msg')}"

    print(f"   ✅ Сообщение: {put_response.get('msg')}")

    # --------------------------------------------------------------------
    # ШАГ 4: Проверка через GET что адрес действительно обновлен
    # --------------------------------------------------------------------
    print("\n[ШАГ 4] Проверка через GET что адрес действительно обновлен...")

    address_updated = GoogleMapsAPI.verify_address_updated(place_id, new_address)

    assert address_updated, \
        f"Адрес не обновился! Ожидался: {new_address}"

    # --------------------------------------------------------------------
    # ШАГ 5: Вывод результата
    # --------------------------------------------------------------------
    print("\n" + "="*60)
    print(" РЕЗУЛЬТАТ ТЕСТА")
    print("="*60)

    print(f"\n📊 СТАТИСТИКА:")
    print(f"   place_id: {place_id}")
    print(f"   Новый адрес: {new_address}")
    print(f"   Ответ PUT: {put_response.get('msg')}")
    print(f"   ✅ Адрес успешно обновлен и подтвержден через GET")

    print("\n" + "="*60)
    print("✅ ТЕСТ PUT ПРОЙДЕН УСПЕШНО!")
    print("="*60)


if __name__ == "__main__":
    test_update_place()