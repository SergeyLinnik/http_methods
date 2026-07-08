# -*- coding: utf-8 -*-
"""
Модуль для работы с Google Maps API.
Содержит методы для выполнения запросов к Google Maps API.
"""

import requests
from src.http_methods import HTTPMethods


class GoogleMapsAPI:
    """
    Класс для работы с Google Maps API.
    Использует HTTPMethods для выполнения запросов.
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
        """
        Создание нового места через POST запрос к Google Maps API.
        """
        url: str = (
            f"{GoogleMapsAPI.BASE_URL}"
            f"/maps/api/place/add/json"
            f"?key={GoogleMapsAPI.API_KEY}"
        )

        body: dict = {
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
        print(f"   Body: {body}")

        response = HTTPMethods.post(url, body)
        print(f"   Статус-код: {response.status_code}")

        response_json: dict = response.json()
        return response_json, response

    # ------------------------------------------------------------------------
    # GET: ПОЛУЧЕНИЕ МЕСТА
    # ------------------------------------------------------------------------

    @staticmethod
    def get_place(place_id: str) -> tuple[dict, requests.Response]:
        """
        Получение данных о месте через GET запрос.
        """
        url: str = (
            f"{GoogleMapsAPI.BASE_URL}"
            f"/maps/api/place/get/json"
            f"?key={GoogleMapsAPI.API_KEY}"
            f"&place_id={place_id}"
        )

        print(f"\n📡 GET запрос к Google Maps API")
        print(f"   URL: {url}")

        response = HTTPMethods.get(url)
        print(f"   Статус-код: {response.status_code}")

        response_json: dict = response.json()
        return response_json, response

    # ------------------------------------------------------------------------
    # PUT: ОБНОВЛЕНИЕ АДРЕСА
    # ------------------------------------------------------------------------

    @staticmethod
    def update_place(place_id: str, new_address: str) -> tuple[dict, requests.Response]:
        """
        Обновление адреса места через PUT запрос.
        """
        url: str = (
            f"{GoogleMapsAPI.BASE_URL}"
            f"/maps/api/place/update/json"
            f"?key={GoogleMapsAPI.API_KEY}"
        )

        body: dict = {
            "place_id": place_id,
            "address": new_address,
            "key": GoogleMapsAPI.API_KEY
        }

        print(f"\n📡 PUT запрос к Google Maps API")
        print(f"   URL: {url}")
        print(f"   Body: {body}")

        response = HTTPMethods.put(url, body)
        print(f"   Статус-код: {response.status_code}")

        response_json: dict = response.json()
        return response_json, response

    # ------------------------------------------------------------------------
    # DELETE: УДАЛЕНИЕ МЕСТА
    # ------------------------------------------------------------------------

    @staticmethod
    def delete_place(place_id: str) -> tuple[dict, requests.Response]:
        """
        Удаление места через DELETE запрос.
        """
        url: str = (
            f"{GoogleMapsAPI.BASE_URL}"
            f"/maps/api/place/delete/json"
            f"?key={GoogleMapsAPI.API_KEY}"
        )

        body: dict = {
            "place_id": place_id
        }

        print(f"\n🗑️ DELETE запрос к Google Maps API")
        print(f"   URL: {url}")
        print(f"   Body: {body}")

        response = HTTPMethods.delete(url, body)
        print(f"   Статус-код: {response.status_code}")

        response_json: dict = response.json()
        return response_json, response