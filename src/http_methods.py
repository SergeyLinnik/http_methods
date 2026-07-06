# -*- coding: utf-8 -*-
"""
Модуль с классом для HTTP запросов.
Содержит только методы GET, POST, PUT, DELETE.
"""

import requests
from typing import Optional


class HTTPMethods:
    """
    Класс для выполнения HTTP запросов.
    Содержит только HTTP методы (GET, POST, PUT, DELETE).
    """

    headers: dict[str, str] = {'Content-Type': 'application/json'}
    cookie: dict[str, str] = {}

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
        return requests.get(url, headers=final_headers, cookies=final_cookies)

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
        return requests.post(url, json=body, headers=final_headers,
                             cookies=final_cookies)

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
        return requests.put(url, json=body, headers=final_headers,
                            cookies=final_cookies)

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
            return requests.delete(url, json=body, headers=final_headers,
                                   cookies=final_cookies)
        return requests.delete(url, headers=final_headers,
                               cookies=final_cookies)