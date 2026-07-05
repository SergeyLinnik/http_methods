# -*- coding: utf-8 -*-
"""
Модуль с классом для HTTP запросов.
Содержит методы GET, POST, PUT, DELETE с headers и cookie.
"""

import requests
from typing import Optional, List, Any


class HTTPMethods:
    """
    Класс для выполнения HTTP запросов.
    Содержит статические методы для GET, POST, PUT, DELETE.
    Использует общие headers и cookie для всех запросов.
    """

    # ------------------------------------------------------------------------
    # ОБЩИЕ НАСТРОЙКИ ДЛЯ ВСЕХ ЗАПРОСОВ
    # ------------------------------------------------------------------------

    headers: dict[str, str] = {'Content-Type': 'application/json'}
    cookie: dict[str, str] = {}

    # ------------------------------------------------------------------------
    # МЕТОД GET
    # ------------------------------------------------------------------------

    @staticmethod
    def get(url: str, headers: Optional[dict[str, str]] = None,
            cookies: Optional[dict[str, str]] = None) -> requests.Response:
        """Выполнение GET запроса."""
        final_headers = HTTPMethods.headers.copy()
        if headers:
            final_headers.update(headers)

        final_cookies = HTTPMethods.cookie.copy()
        if cookies:
            final_cookies.update(cookies)

        result = requests.get(url, headers=final_headers, cookies=final_cookies)
        return result

    # ------------------------------------------------------------------------
    # МЕТОД POST
    # ------------------------------------------------------------------------

    @staticmethod
    def post(url: str, body: dict,
             headers: Optional[dict[str, str]] = None,
             cookies: Optional[dict[str, str]] = None) -> requests.Response:
        """Выполнение POST запроса."""
        final_headers = HTTPMethods.headers.copy()
        if headers:
            final_headers.update(headers)

        final_cookies = HTTPMethods.cookie.copy()
        if cookies:
            final_cookies.update(cookies)

        result = requests.post(url, json=body, headers=final_headers,
                               cookies=final_cookies)
        return result

    # ------------------------------------------------------------------------
    # МЕТОД PUT
    # ------------------------------------------------------------------------

    @staticmethod
    def put(url: str, body: dict,
            headers: Optional[dict[str, str]] = None,
            cookies: Optional[dict[str, str]] = None) -> requests.Response:
        """Выполнение PUT запроса."""
        final_headers = HTTPMethods.headers.copy()
        if headers:
            final_headers.update(headers)

        final_cookies = HTTPMethods.cookie.copy()
        if cookies:
            final_cookies.update(cookies)

        result = requests.put(url, json=body, headers=final_headers,
                              cookies=final_cookies)
        return result

    # ------------------------------------------------------------------------
    # МЕТОД DELETE
    # ------------------------------------------------------------------------

    @staticmethod
    def delete(url: str, body: Optional[dict] = None,
               headers: Optional[dict[str, str]] = None,
               cookies: Optional[dict[str, str]] = None) -> requests.Response:
        """Выполнение DELETE запроса."""
        final_headers = HTTPMethods.headers.copy()
        if headers:
            final_headers.update(headers)

        final_cookies = HTTPMethods.cookie.copy()
        if cookies:
            final_cookies.update(cookies)

        if body:
            result = requests.delete(url, json=body, headers=final_headers,
                                     cookies=final_cookies)
        else:
            result = requests.delete(url, headers=final_headers,
                                     cookies=final_cookies)
        return result

    # ------------------------------------------------------------------------
    # МЕТОД ПРОВЕРКИ СТАТУС-КОДА
    # ------------------------------------------------------------------------

    @staticmethod
    def check_status_code(response: requests.Response, expected_status: int) -> bool:
        """
        Проверка статус-кода ответа.

        Args:
            response: Response объект
            expected_status: Ожидаемый статус-код

        Returns:
            True если статус-код совпадает

        Raises:
            AssertionError: Если статус-код не совпадает
        """
        actual_status: int = response.status_code

        print(f"\n🔍 Проверка статус-кода:")
        print(f"   Ожидаемый статус: {expected_status}")
        print(f"   Фактический статус: {actual_status}")

        assert actual_status == expected_status, \
            f"Статус-код не совпадает! Ожидался {expected_status}, получен {actual_status}"

        print(f"   ✅ Статус-код {actual_status} соответствует ожидаемому")
        return True

    # ------------------------------------------------------------------------
    # НОВЫЙ МЕТОД: ПРОВЕРКА НАЛИЧИЯ ОБЯЗАТЕЛЬНЫХ ПОЛЕЙ
    # ------------------------------------------------------------------------

    @staticmethod
    def check_required_fields(data: dict, required_fields: List[str]) -> bool:
        """
        Проверка наличия обязательных полей в словаре.

        Args:
            data: Словарь с данными для проверки
            required_fields: Список обязательных полей

        Returns:
            True если все поля присутствуют

        Raises:
            AssertionError: Если какое-то поле отсутствует
        """
        print(f"\n🔍 Проверка наличия обязательных полей:")
        print(f"   Обязательные поля: {required_fields}")
        print(f"   Поля в ответе: {list(data.keys())}")

        missing_fields: List[str] = []

        for field in required_fields:
            if field not in data:
                missing_fields.append(field)

        assert not missing_fields, \
            f"Отсутствуют обязательные поля: {missing_fields}"

        print(f"   ✅ Все обязательные поля присутствуют")
        return True