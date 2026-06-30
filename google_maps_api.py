# -*- coding: utf-8 -*-
"""
Модуль для работы с Google Maps API.
Содержит методы для выполнения запросов к Google Maps API.
"""

from typing import Optional

from http_methods import HTTPMethods


class GoogleMapsAPI:
    """
    Класс для работы с Google Maps API.
    Использует HTTPMethods для выполнения запросов.
    """

    # ------------------------------------------------------------------------
    # БАЗОВЫЕ НАСТРОЙКИ API
    # ------------------------------------------------------------------------

    BASE_URL: str = "https://rahulshettyacademy.com"
    API_KEY: str = "qaclick123"

    # ------------------------------------------------------------------------
    # МЕТОД POST: СОЗДАНИЕ МЕСТА
    # ------------------------------------------------------------------------

    @staticmethod
    def create_place(lat: float = -38.383494,
                     lng: float = 33.427362,
                     name: str = "Frontline house",
                     address: str = "29, side layout, cohen 09") -> dict:
        """
        Создание нового места через POST запрос к Google Maps API.

        Args:
            lat: Широта (по умолчанию -38.383494)
            lng: Долгота (по умолчанию 33.427362)
            name: Название места (по умолчанию "Frontline house")
            address: Адрес (по умолчанию "29, side layout, cohen 09")

        Returns:
            Ответ API в виде словаря

        Raises:
            AssertionError: Если запрос не удался
        """
        url: str = (
            f"{GoogleMapsAPI.BASE_URL}"
            f"/maps/api/place/add/json"
            f"?key={GoogleMapsAPI.API_KEY}"
        )

        body: dict = {
            "location": {
                "lat": lat,
                "lng": lng
            },
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
        print(f"   Body: {body}")

        # Выполнение POST запроса через HTTPMethods
        response = HTTPMethods.post(url, body)

        print(f"   Статус-код: {response.status_code}")

        # Проверка через assert (без try-except)
        assert response.status_code == 200, \
            f"Ожидался статус 200, получен {response.status_code}"

        response_json: dict = response.json()
        assert response_json.get("status") == "OK", \
            f"Статус ответа не 'OK': {response_json}"

        place_id: str = response_json.get("place_id")
        assert place_id is not None, "В ответе отсутствует поле place_id"

        print(f"   ✅ Место создано! place_id: {place_id}")
        return response_json