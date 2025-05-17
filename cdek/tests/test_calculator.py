from typing import Any
from cdek import CDEKCalculator


def test__fetch_alltariffs_returns_some_tariffs(
    calculator: CDEKCalculator,
) -> None:
    """fetch_alltariffs"""
    alltariffs = calculator.fetch_alltariffs()
    assert alltariffs is not None and len(alltariffs.tariff_codes) > 0


def test__fetch_tariff_returns_calculate(
    calculator: CDEKCalculator,
    from_location: dict[str, Any],
    to_location: dict[str, Any],
    packages: list[dict[str, Any]],
) -> None:
    """fetch_tariff"""
    tariff = calculator.fetch_tariff(
        {
            "tariff_code": 139,
            "from_location": from_location,
            "to_location": to_location,
            "packages": packages,
        }
    )
    assert tariff is not None


def test__fetch_tarifflist_returns_calculate(
    calculator: CDEKCalculator,
    from_location: dict[str, Any],
    to_location: dict[str, Any],
    packages: list[dict[str, Any]],
) -> None:
    """fetch_tarifflist"""
    tariff = calculator.fetch_tarifflist(
        {
            "from_location": from_location,
            "to_location": to_location,
            "packages": packages,
        }
    )
    assert tariff is not None
