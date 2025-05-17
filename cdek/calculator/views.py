from typing import Any
import json
import httpx
from cdek._base import CDEKBase
from cdek.calculator.schemas import (
    TariffListCodes,
    TariffCode,
    AllTariffCodes,
)


class CDEKCalculator(CDEKBase):
    def fetch_tarifflist(self, params: dict[str, Any]) -> TariffListCodes | None:
        """/v2/calculator/tarifflist

        date
        string <date-time> yyyy-MM-dd'T'HH:mm:ssZ
        Дата и время планируемой передачи заказа. По умолчанию - текущая

        type
        integer <int32>
        Тип заказа.
        1 - интернет-магазин,
        2 - доставка.
        По умолчанию - 1

        additional_order_types
        Array of integers <int32> unique [ items <int32 > ]
        Дополнительный тип заказа:
        2 - для сборного груза (LTL);
        4 - для Forward;
        6 - для "Фулфилмент. Приход";
        7 - для "Фулфилмент. Отгрузка";
        10 - для доставки шин по тарифу "Экономичный экспресс";
        11 - для доставки в рамках одного офиса "Один офис (ИМ)" (при условии, что офис отправителя и получателя совпадают);
        14 - для CDEK.Shopping

        currency
        integer <int32>
        Валюта, в которой необходимо произвести расчет.
        По умолчанию - валюта договора

        lang
        string <= 3 characters
        Язык вывода информации о тарифах.
        Возможные значения: rus, eng, zho.
        По умолчанию - rus

        *from_location
        object (CalculatorLocationDto)
        Населённый пункт для вычислений тарифа

        *to_location
        object (CalculatorLocationDto)
        Населённый пункт для вычислений тарифа

        *packages
        Array of objects (CalcPackageRequestDto)
        Места (упаковки) в заказе
        """

        try:
            responce = httpx.post(
                url=self._fetch_base_url() + "/v2/calculator/tarifflist",
                headers=self._fetch_base_header(),
                content=json.dumps(params),
            )
        except httpx.ReadTimeout:
            return None
        if responce.status_code != httpx.codes.OK:
            return None
        if len(responce.json()) == 0:
            return None
        return TariffListCodes(**responce.json())

    def fetch_tariff(self, params: dict[str, Any]) -> TariffCode | None:
        """/v2/calculator/tariff

        date
        string <date-time> yyyy-MM-dd'T'HH:mm:ssZ
        Дата и время планируемой передачи заказа. По умолчанию - текущая

        type
        integer <int32>
        Тип заказа.
        1 - интернет-магазин,
        2 - доставка.
        По умолчанию - 1

        currency
        integer <int32>
        Валюта, в которой необходимо произвести расчет.
        По умолчанию - валюта договора

        lang
        string <= 3 characters
        Язык вывода информации о тарифах.
        Возможные значения: rus, eng, zho.
        По умолчанию - rus

        *tariff_code
        integer <int32>
        Код тарифа. Обязателен для расчета по коду тарифа

        *from_location
        object (CalculatorLocationDto)
        Населённый пункт для вычислений тарифа

        *to_location
        object (CalculatorLocationDto)
        Населённый пункт для вычислений тарифа

        services
        Array of objects (CalcAdditionalServiceDto)
        Дополнительные услуги

        *packages
        Array of objects (CalcPackageRequestDto)
        Места (упаковки) в заказе

        additional_order_types
        Array of integers <int32> unique [ items <int32 > ]
        Дополнительный тип заказа:
        2 - для сборного груза (LTL);
        4 - для Forward;
        6 - для "Фулфилмент. Приход";
        7 - для "Фулфилмент. Отгрузка";
        10 - для доставки шин по тарифу "Экономичный экспресс";
        11 - для доставки в рамках одного офиса "Один офис (ИМ)" (при условии, что офис отправителя и получателя совпадают);
        14 - для CDEK.Shopping
        """
        try:
            responce = httpx.post(
                url=self._fetch_base_url() + "/v2/calculator/tariff",
                headers=self._fetch_base_header(),
                content=json.dumps(params),
            )
        except httpx.ReadTimeout:
            return None
        if responce.status_code != httpx.codes.OK:
            return None
        if len(responce.json()) == 0:
            return None
        return TariffCode(**responce.json())

    def fetch_alltariffs(self) -> AllTariffCodes | None:
        """/v2/calculator/alltariffs"""
        try:
            responce = httpx.get(
                url=self._fetch_base_url() + "/v2/calculator/alltariffs",
                headers=self._fetch_base_header(),
            )
        except httpx.ReadTimeout:
            return None
        if responce.status_code != httpx.codes.OK:
            return None
        if len(responce.json()) == 0:
            return None
        return AllTariffCodes(**responce.json())
