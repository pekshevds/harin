from typing import Any
import httpx
from cdek._base import CDEKBase
from cdek.location.schemas import (
    Region,
    City,
    PostalCode,
    SuggestCity,
)


class CDEKLocation(CDEKBase):
    def fetch_regions(self, params: dict[str, Any] | None) -> list[Region] | None:
        """/v2/location/regions

        country_codes
        Array of strings
        Массив кодов стран в формате ISO_3166-1_alpha-2

        size
        number <integer>
        Ограничение выборки результата. По умолчанию 1000. Обязателен, если указан page

        page
        number <integer>
        Номер страницы выборки результата. По умолчанию 0

        lang
        string <= 3 characters
        Локализация. По умолчанию rus (доступны eng и zho)
        """
        responce = httpx.get(
            url=self._fetch_base_url() + "/v2/location/regions",
            headers=self._fetch_base_header(),
            params=params,
        )
        if responce.status_code != httpx.codes.OK:
            return None
        if len(responce.json()) == 0:
            return None
        return [Region(**record) for record in responce.json()]

    def fetch_cities(self, params: dict[str, Any] | None) -> list[City] | None:
        """/v2/location/cities

        country_codes
        Array of strings
        Массив кодов стран в формате ISO_3166-1_alpha-2

        region_code
        integer <int32>
        Код региона (справочник СДЭК)

        fias_guid
        string <uuid>
        Уникальный идентификатор ФИАС населенного пункта

        postal_code
        string <= 255 characters
        Почтовый индекс

        code
        integer <int32>
        Код населенного пункта СДЭК

        city
        string <= 255 characters
        Название населенного пункта. Должно соответствовать полностью

        payment_limit
        number <double>
        Ограничение на сумму наложенного платежа. -1 - ограничения нет; 0 - наложенный платеж не принимается;

        size
        integer <int32>
        Ограничение выборки результата. По умолчанию 1000. Обязателен, если указан page

        page
        integer <int32>
        Номер страницы выборки результата. По умолчанию 0

        lang
        string <= 3 characters
        Язык локализации ответа
        """
        responce = httpx.get(
            url=self._fetch_base_url() + "/v2/location/cities",
            headers=self._fetch_base_header(),
            params=params,
        )
        if responce.status_code != httpx.codes.OK:
            return None
        if len(responce.json()) == 0:
            return None
        return [City(**record) for record in responce.json()]

    def fetch_postalcodes(self, params: dict[str, Any]) -> PostalCode | None:
        """/v2/location/postalcodes

        *code
        integer <int32>
        Код города, которому принадлежат почтовые индексы
        """
        responce = httpx.get(
            url=self._fetch_base_url() + "/v2/location/postalcodes",
            headers=self._fetch_base_header(),
            params=params,
        )
        if responce.status_code != httpx.codes.OK:
            return None
        if len(responce.json()) == 0:
            return None
        return PostalCode(**responce.json())

    def fetch_suggest_cities(self, params: dict[str, Any]) -> list[SuggestCity] | None:
        """/v2/location/suggest/cities

        *name
        string <= 255 characters
        Наименование населенного пункта СДЭК

        country_code
        string <= 2 characters
        Код страны в формате ISO_3166-1_alpha-2
        """
        responce = httpx.get(
            url=self._fetch_base_url() + "/v2/location/suggest/cities",
            headers=self._fetch_base_header(),
            params=params,
        )
        if responce.status_code != httpx.codes.OK:
            return None
        if len(responce.json()) == 0:
            return None
        return [SuggestCity(**record) for record in responce.json()]
