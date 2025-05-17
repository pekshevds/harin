from typing import Any
import httpx
from cdek._base import CDEKBase
from cdek.deliverypoint.schemas import DeliveryPoint


class CDEKDeliveryPoint(CDEKBase):
    def fetch_deliverypoints(
        self, params: dict[str, Any]
    ) -> list[DeliveryPoint] | None:
        """/v2/deliverypoints
        code
        string
        Example: code=NSK1
        Код ПВЗ

        type
        string
        Example: type=DeliveryPointType.ALL
        Тип офиса. Принимает значения "POSTAMAT", "PVZ", "ALL". При отсутствии параметра принимается значение по умолчанию DeliveryPointType.ALL.

        postal_code
        string
        Example: postal_code=630000
        Почтовый индекс города, для которого необходим список офисов

        city_code
        integer <int32>
        Example: city_code=270
        Код населенного пункта СДЭК (метод "Список населенных пунктов")

        country_code
        string
        Example: country_code=RU
        Код страны в формате ISO_3166-1_alpha-2 (см. “Общероссийский классификатор стран мира”)

        region_code
        integer <int32>
        Example: region_code=5
        Код региона СДЭК

        have_cashless
        boolean
        Example: have_cashless=true
        Наличие терминала оплаты. Может принимать значения: «1», «true» - есть; «0», «false» - нет.

        have_cash
        boolean
        Example: have_cash=true
        Есть прием наличных. Может принимать значения: «1», «true» - есть; «0», «false» - нет.

        allowed_cod
        boolean
        Example: allowed_cod=true
        Разрешен наложенный платеж. Может принимать значения: «1», «true» - есть; «0», «false» - нет.

        is_dressing_room
        boolean
        Example: is_dressing_room=true
        Наличие примерочной. Может принимать значения: «1», «true» - есть; «0», «false» - нет.

        weight_max
        integer <int32>
        Example: weight_max=10
        Максимальный вес в кг, который может принять офис (значения больше 0 - передаются офисы, которые принимают этот вес; 0 - офисы с нулевым весом не передаются; значение не указано - все офисы)

        weight_min
        integer <int32>
        Example: weight_min=5
        Минимальный вес в кг, который принимает офис (при переданном значении будут выводиться офисы с минимальным весом до указанного значения)

        lang
        string
        Example: lang=rus
        Локализация офиса.

        take_only
        boolean
        Example: take_only=true
        Является ли офис только пунктом выдачи. Может принимать значения: «1», «true» - есть; «0», «false» - нет.

        is_handout
        boolean
        Example: is_handout=true
        Является пунктом выдачи. Может принимать значения: «1», «true» - есть; «0», «false» - нет.

        is_reception
        boolean
        Example: is_reception=true
        Есть ли в офисе приём заказов. Может принимать значения: «1», «true» - есть; «0», «false» - нет.

        is_marketplace
        boolean
        Example: is_marketplace=true
        Офис для доставки "До маркетплейса". Может принимать значения: «1», «true» - есть; «0», «false» - нет.

        is_ltl
        boolean
        Example: is_ltl=true
        Работает ли офис с LTL (сборный груз). Может принимать значения: «1», «true» - есть; «0», «false» - нет.

        fulfillment
        boolean
        Example: fulfillment=true
        Офис с зоной фулфилмента. Может принимать значения: «1», «true» - есть; «0», «false» - нет.

        fias_guid
        string <uuid>
        Example: fias_guid=e33970a6-0db6-4e35-832c-cc3312a1833e
        Код города ФИАС

        size
        integer <int32>
        Example: size=1000
        Ограничение выборки результата (размер страницы)

        page
        integer <int32>
        Example: page=2
        Номер страницы выборки результата
        """
        if len(params.items()) == 0:
            return None
        responce = httpx.get(
            url=self._fetch_base_url() + "/v2/deliverypoints",
            headers=self._fetch_base_header(),
            params=params,
        )
        if responce.status_code != httpx.codes.OK:
            return None
        if len(responce.json()) == 0:
            return None
        return [DeliveryPoint(**record) for record in responce.json()]
