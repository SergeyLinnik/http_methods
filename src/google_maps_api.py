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

    @staticmethod
    def create_place(lat: float = -38.383494,
                     lng: float = 33.427362,
                     name: str = "Frontline house",
                     address: str = "29, side layout, cohen 09") -> tuple[dict, requests.Response]:
        """
        Создание нового места через POST запрос к Google Maps API.

        Returns:
            Кортеж (ответ API в виде словаря, response объект)
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

        response = HTTPMethods.post(url, body)

        print(f"   Статус-код: {response.status_code}")

        assert response.status_code == 200, \
            f"Ожидался статус 200, получен {response.status_code}"

        response_json: dict = response.json()
        assert response_json.get("status") == "OK", \
            f"Статус ответа не 'OK': {response_json}"

        place_id: str = response_json.get("place_id")
        assert place_id is not None, "В ответе отсутствует поле place_id"

        print(f"   ✅ Место создано! place_id: {place_id}")
        return response_json, response