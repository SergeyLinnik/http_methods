# -*- coding: utf-8 -*-
"""
Модуль с классом для HTTP запросов.
Содержит методы GET, POST, PUT, DELETE с headers и cookie.
"""

import requests
from typing import Optional, Dict, Any


class HTTP_methods:
    """
    Класс для выполнения HTTP запросов.
    Содержит статические методы для GET, POST, PUT, DELETE.
    Использует общие headers и cookie для всех запросов.
    """

    # ------------------------------------------------------------------------
    # ОБЩИЕ НАСТРОЙКИ ДЛЯ ВСЕХ ЗАПРОСОВ
    # ------------------------------------------------------------------------

    headers: Dict[str, str] = {'Content-Type': 'application/json'}
    cookie: Dict[str, str] = {}

    # ------------------------------------------------------------------------
    # МЕТОД GET
    # ------------------------------------------------------------------------

    @staticmethod
    def get(url: str, headers: Optional[Dict[str, str]] = None,
            cookies: Optional[Dict[str, str]] = None) -> requests.Response:
        """
        Выполнение GET запроса.

        Args:
            url: URL для запроса
            headers: Дополнительные headers (опционально)
            cookies: Дополнительные cookies (опционально)

        Returns:
            Response объект
        """
        final_headers = HTTP_methods.headers.copy()
        if headers:
            final_headers.update(headers)

        final_cookies = HTTP_methods.cookie.copy()
        if cookies:
            final_cookies.update(cookies)

        result = requests.get(url, headers=final_headers, cookies=final_cookies)
        return result

    # ------------------------------------------------------------------------
    # МЕТОД POST
    # ------------------------------------------------------------------------

    @staticmethod
    def post(url: str, body: Dict[str, Any],
             headers: Optional[Dict[str, str]] = None,
             cookies: Optional[Dict[str, str]] = None) -> requests.Response:
        """
        Выполнение POST запроса.

        Args:
            url: URL для запроса
            body: Тело запроса (JSON)
            headers: Дополнительные headers (опционально)
            cookies: Дополнительные cookies (опционально)

        Returns:
            Response объект
        """
        final_headers = HTTP_methods.headers.copy()
        if headers:
            final_headers.update(headers)

        final_cookies = HTTP_methods.cookie.copy()
        if cookies:
            final_cookies.update(cookies)

        result = requests.post(url, json=body, headers=final_headers,
                               cookies=final_cookies)
        return result

    # ------------------------------------------------------------------------
    # МЕТОД PUT
    # ------------------------------------------------------------------------

    @staticmethod
    def put(url: str, body: Dict[str, Any],
            headers: Optional[Dict[str, str]] = None,
            cookies: Optional[Dict[str, str]] = None) -> requests.Response:
        """
        Выполнение PUT запроса.

        Args:
            url: URL для запроса
            body: Тело запроса (JSON)
            headers: Дополнительные headers (опционально)
            cookies: Дополнительные cookies (опционально)

        Returns:
            Response объект
        """
        final_headers = HTTP_methods.headers.copy()
        if headers:
            final_headers.update(headers)

        final_cookies = HTTP_methods.cookie.copy()
        if cookies:
            final_cookies.update(cookies)

        result = requests.put(url, json=body, headers=final_headers,
                              cookies=final_cookies)
        return result

    # ------------------------------------------------------------------------
    # МЕТОД DELETE
    # ------------------------------------------------------------------------

    @staticmethod
    def delete(url: str, body: Optional[Dict[str, Any]] = None,
               headers: Optional[Dict[str, str]] = None,
               cookies: Optional[Dict[str, str]] = None) -> requests.Response:
        """
        Выполнение DELETE запроса.

        Args:
            url: URL для запроса
            body: Тело запроса (JSON, опционально)
            headers: Дополнительные headers (опционально)
            cookies: Дополнительные cookies (опционально)

        Returns:
            Response объект
        """
        final_headers = HTTP_methods.headers.copy()
        if headers:
            final_headers.update(headers)

        final_cookies = HTTP_methods.cookie.copy()
        if cookies:
            final_cookies.update(cookies)

        if body:
            result = requests.delete(url, json=body, headers=final_headers,
                                     cookies=final_cookies)
        else:
            result = requests.delete(url, headers=final_headers,
                                     cookies=final_cookies)
        return result