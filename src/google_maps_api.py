# -*- coding: utf-8 -*-
"""
Модуль для работы с Google Maps API.
"""

import requests
from src.http_methods import HTTPMethods


class GoogleMapsAPI:
    """
    Класс для работы с Google Maps API.
    """

    BASE_URL: str = "https://rahulshettyacademy.com"
    API_KEY: str = "qaclick123"

    # ------------------------------------------------------------------------
    # POST: СОЗДАНИЕ МЕСТА
    # ------------------------------------------------------------------------

    @staticmethod
    def create_place(lat: float = -38.383494,
                     lng: float = 33.427362,
                     name: str = "Frontline house",
                     address: str = "29, side layout, cohen 09") -> tuple[dict, requests.Response]:
        """Создание места через POST."""
        url = f"{GoogleMapsAPI.BASE_URL}/maps/api/place/add/json?key={GoogleMapsAPI.API_KEY}"
        body = {
            "location": {"lat": lat, "lng": lng},
            "accuracy": 50,
            "name": name,
            "phone_number": "(+91) 983 893 3937",
            "address": address,
            "types": ["shoe park", "shop"],
            "website": "http://google.com",
            "language": "French-IN"
        }
        print(f"\n📡 POST запрос к Google Maps API")
        print(f"   URL: {url}")
        response = HTTPMethods.post(url, body)
        print(f"   Статус-код: {response.status_code}")
        assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"
        response_json = response.json()
        assert response_json.get("status") == "OK"
        place_id = response_json.get("place_id")
        assert place_id is not None
        print(f"   ✅ Место создано! place_id: {place_id}")
        return response_json, response

    # ------------------------------------------------------------------------
    # GET: ПОЛУЧЕНИЕ МЕСТА
    # ------------------------------------------------------------------------

    @staticmethod
    def get_place(place_id: str) -> tuple[dict, requests.Response]:
        """Получение места через GET."""
        url = f"{GoogleMapsAPI.BASE_URL}/maps/api/place/get/json?key={GoogleMapsAPI.API_KEY}&place_id={place_id}"
        print(f"\n📡 GET запрос к Google Maps API")
        print(f"   URL: {url}")
        response = HTTPMethods.get(url)
        print(f"   Статус-код: {response.status_code}")
        assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"
        response_json = response.json()
        if "msg" in response_json:
            assert False, f"Место не найдено: {response_json.get('msg')}"
        print(f"   ✅ Данные о месте получены")
        return response_json, response

    # ------------------------------------------------------------------------
    # PUT: ОБНОВЛЕНИЕ АДРЕСА
    # ------------------------------------------------------------------------

    @staticmethod
    def update_place(place_id: str, new_address: str) -> tuple[dict, requests.Response]:
        """Обновление адреса через PUT."""
        url = f"{GoogleMapsAPI.BASE_URL}/maps/api/place/update/json?key={GoogleMapsAPI.API_KEY}"
        body = {
            "place_id": place_id,
            "address": new_address,
            "key": GoogleMapsAPI.API_KEY
        }
        print(f"\n📡 PUT запрос к Google Maps API")
        print(f"   URL: {url}")
        print(f"   Body: {body}")
        response = HTTPMethods.put(url, body)
        print(f"   Статус-код: {response.status_code}")
        assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"
        response_json = response.json()
        assert "msg" in response_json
        assert "updated" in response_json["msg"].lower()
        print(f"   ✅ Адрес обновлен: {response_json.get('msg')}")
        return response_json, response

    # ------------------------------------------------------------------------
    # DELETE: УДАЛЕНИЕ МЕСТА
    # ------------------------------------------------------------------------

    @staticmethod
    def delete_place(place_id: str) -> tuple[dict, requests.Response]:
        """Удаление места через DELETE."""
        url = f"{GoogleMapsAPI.BASE_URL}/maps/api/place/delete/json?key={GoogleMapsAPI.API_KEY}"
        body = {"place_id": place_id}
        print(f"\n🗑️ DELETE запрос к Google Maps API")
        print(f"   URL: {url}")
        print(f"   Body: {body}")
        response = HTTPMethods.delete(url, body)
        print(f"   Статус-код: {response.status_code}")
        assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"
        response_json = response.json()
        assert response_json.get("status") == "OK"
        print(f"   ✅ Место удалено!")
        return response_json, response