from typing import Any
from django.conf import settings
from cdek.location import CDEKLocation, Region, City, PostalCode, SuggestCity
from cdek.deliverypoint import CDEKDeliveryPoint, DeliveryPoint
from cdek.calculator import CDEKCalculator, AllTariffCodes, TariffListCodes, TariffCode


def fetch_cdek_regions() -> list[Region] | None:
    if settings.CDEK_TOKEN.need_update_token():
        settings.CDEK_TOKEN.update_token()
    location = CDEKLocation(settings.CDEK_TOKEN)
    return location.fetch_regions({"country_codes": ["RU"]})


def fetch_cdek_cities(region_code: int) -> list[City] | None:
    if settings.CDEK_TOKEN.need_update_token():
        settings.CDEK_TOKEN.update_token()
    location = CDEKLocation(settings.CDEK_TOKEN)
    return location.fetch_cities({"region_code": region_code})


def fetch_cdek_postalcodes(city_code: int) -> PostalCode | None:
    if settings.CDEK_TOKEN.need_update_token():
        settings.CDEK_TOKEN.update_token()
    location = CDEKLocation(settings.CDEK_TOKEN)
    return location.fetch_postalcodes({"code": city_code})


def fetch_cdek_suggestcities(name: str) -> list[SuggestCity] | None:
    if settings.CDEK_TOKEN.need_update_token():
        settings.CDEK_TOKEN.update_token()
    location = CDEKLocation(settings.CDEK_TOKEN)
    return location.fetch_suggest_cities({"name": name, "country_code": "RU"})


def fetch_cdek_deliverypoints(city_code: int) -> list[DeliveryPoint] | None:
    if settings.CDEK_TOKEN.need_update_token():
        settings.CDEK_TOKEN.update_token()
    deliverypoint = CDEKDeliveryPoint(settings.CDEK_TOKEN)
    return deliverypoint.fetch_deliverypoints({"city_code": city_code})


def fetch_cdek_alltariffs() -> AllTariffCodes | None:
    if settings.CDEK_TOKEN.need_update_token():
        settings.CDEK_TOKEN.update_token()
    calculator = CDEKCalculator(settings.CDEK_TOKEN)
    return calculator.fetch_alltariffs()


def fetch_cdek_tarifflist(data: dict[str, Any]) -> TariffListCodes | None:
    if settings.CDEK_TOKEN.need_update_token():
        settings.CDEK_TOKEN.update_token()
    calculator = CDEKCalculator(settings.CDEK_TOKEN)
    return calculator.fetch_tarifflist(data)


def fetch_cdek_tariff(data: dict[str, Any]) -> TariffCode | None:
    if settings.CDEK_TOKEN.need_update_token():
        settings.CDEK_TOKEN.update_token()
    calculator = CDEKCalculator(settings.CDEK_TOKEN)
    return calculator.fetch_tariff(data)
