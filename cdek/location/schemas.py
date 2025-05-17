from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, kw_only=True)
class Region:
    region: str
    region_code: int = 0
    country: str
    country_code: str


@dataclass(frozen=True, kw_only=True)
class City:
    code: int
    city_uuid: str
    kladr_code: str = ""
    city: str
    fias_guid: str = ""
    country_code: str
    country: str
    region: str = ""
    region_code: int = 0
    sub_region: str = ""
    longitude: Decimal = Decimal("0")
    latitude: Decimal = Decimal("0")
    time_zone: str = ""
    payment_limit: Decimal


@dataclass(frozen=True, kw_only=True)
class PostalCode:
    code: int
    postal_codes: list[str]


@dataclass(frozen=True, kw_only=True)
class SuggestCity:
    city_uuid: str
    code: int
    full_name: str
