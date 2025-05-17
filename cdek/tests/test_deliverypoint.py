from cdek import (
    CDEKDeliveryPoint,
)


def test__fetch_deliverypoints_returns_deliverypoints_for_nsk1(
    deliverypoint: CDEKDeliveryPoint,
) -> None:
    """fetch_regions"""
    deliverypoints_for_nsk1 = deliverypoint.fetch_deliverypoints({"code": "NSK1"})
    assert deliverypoints_for_nsk1 is not None and len(deliverypoints_for_nsk1) > 0


def test__fetch_deliverypoints_returns_none_for_unknown_code(
    deliverypoint: CDEKDeliveryPoint,
) -> None:
    """fetch_regions"""
    deliverypoints_for_nsk1 = deliverypoint.fetch_deliverypoints({"code": "unknown"})
    assert deliverypoints_for_nsk1 is None


def test__fetch_deliverypoints_returns_none_without_params(
    deliverypoint: CDEKDeliveryPoint,
) -> None:
    """fetch_regions"""
    assert deliverypoint.fetch_deliverypoints({}) is None
