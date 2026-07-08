# -*- coding: utf-8 -*-
"""
Вспомогательные методы для тестирования.
Содержат проверки статус-кода, обязательных полей и содержимого полей.
"""

import requests
from typing import List, Any, Optional


class TestHelpers:
    """
    Класс с вспомогательными методами для тестов.
    Содержит проверки, которые используются в тестах.
    """

    @staticmethod
    def check_status_code(response: requests.Response, expected_status: int) -> None:
        """
        Проверка статус-кода ответа.

        Args:
            response: Response объект
            expected_status: Ожидаемый статус-код

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

    @staticmethod
    def check_required_fields(data: dict, required_fields: List[str]) -> None:
        """
        Проверка наличия обязательных полей в словаре.

        Args:
            data: Словарь с данными для проверки
            required_fields: Список обязательных полей

        Raises:
            AssertionError: Если какое-то поле отсутствует
        """
        print(f"\n🔍 Проверка наличия обязательных полей:")
        print(f"   Обязательные поля: {required_fields}")
        print(f"   Поля в ответе: {list(data.keys())}")

        missing_fields: List[str] = [f for f in required_fields if f not in data]

        assert not missing_fields, \
            f"Отсутствуют обязательные поля: {missing_fields}"
        print(f"   ✅ Все обязательные поля присутствуют")

    # ------------------------------------------------------------------------
    # НОВЫЙ МЕТОД: ПРОВЕРКА СОДЕРЖИМОГО ПОЛЕЙ
    # ------------------------------------------------------------------------

    @staticmethod
    def check_field_value(data: dict, field_name: str, expected_value: Any,
                          field_description: Optional[str] = None) -> None:
        """
        Проверка значения конкретного поля в словаре.

        Args:
            data: Словарь с данными для проверки
            field_name: Имя проверяемого поля
            expected_value: Ожидаемое значение поля
            field_description: Описание поля (для вывода, опционально)

        Raises:
            AssertionError: Если поле отсутствует или значение не совпадает
        """
        field_desc: str = field_description or field_name
        actual_value: Any = data.get(field_name)

        print(f"\n🔍 Проверка содержимого поля '{field_desc}':")
        print(f"   Ожидаемое значение: {expected_value}")
        print(f"   Фактическое значение: {actual_value}")

        assert field_name in data, \
            f"Поле '{field_name}' отсутствует в ответе"

        assert actual_value == expected_value, \
            f"Значение поля '{field_name}' не совпадает! " \
            f"Ожидалось: {expected_value}, получено: {actual_value}"

        print(f"   ✅ Поле '{field_desc}' содержит ожидаемое значение")