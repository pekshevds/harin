from cdek import (
    CDEKLocation,
)


def test__fetch_regions_returns_russian_regions(location: CDEKLocation) -> None:
    """fetch_regions"""
    regions = location.fetch_regions({"country_codes": ["RU"]})
    assert regions is not None and len(regions) > 0


def test__fetch_regions_returns_empty_list_of_regions(location: CDEKLocation) -> None:
    """fetch_regions"""
    regions = location.fetch_regions({"country_codes": ["XX"]})
    assert regions is None


def test__fetch_regions_returns_none_without_paramas(location: CDEKLocation) -> None:
    """fetch_regions"""
    regions = location.fetch_regions(None)
    assert regions is not None


def test__fetch_cities_returns_russian_cities(location: CDEKLocation) -> None:
    """fetch_cities"""
    cities = location.fetch_cities({"country_codes": ["RU"]})
    assert cities is not None and len(cities) > 0


def test__fetch_cities_returns_empty_list_of_cities(location: CDEKLocation) -> None:
    """fetch_cities"""
    regions = location.fetch_regions({"country_codes": ["XX"]})
    assert regions is None


def test__fetch_cities_returns_none_without_params(location: CDEKLocation) -> None:
    """fetch_cities"""
    regions = location.fetch_regions(None)
    assert regions is not None


def test__fetch_postalcodes_returns_not_empty(location: CDEKLocation) -> None:
    """fetch_postalcodes
    81921 - Малая Сунь
    """
    postalcodes = location.fetch_postalcodes({"code": 81921})
    assert postalcodes is not None


def test__fetch_postalcodes_returns_empty(location: CDEKLocation) -> None:
    """fetch_postalcodes
    81921 - Малая Сунь
    """
    postalcodes = location.fetch_postalcodes({"code": 0})
    assert postalcodes is None


def test__fetch_suggest_cities(location: CDEKLocation) -> None:
    """fetch_suggest_cities"""
    assert (
        location.fetch_suggest_cities({"name": "Круглое Поле", "country_code": "RU"})
        is not None
    )

    assert location.fetch_suggest_cities({"name": "Круглое Поле"}) is not None
