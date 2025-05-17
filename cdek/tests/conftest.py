from typing import Any
import pytest
from cdek import (
    fetch_fake_client_id,
    fetch_fake_client_secret,
    CDEKAuth,
    CDEKToken,
    CDEKLocation,
    CDEKDeliveryPoint,
    CDEKCalculator,
)


@pytest.fixture()
def fake_token() -> CDEKToken:
    return CDEKToken(
        CDEKAuth(
            client_id=fetch_fake_client_id(), client_secret=fetch_fake_client_secret()
        )
    )


@pytest.fixture()
def location(fake_token: CDEKToken) -> CDEKLocation:
    return CDEKLocation(token=fake_token)


@pytest.fixture()
def deliverypoint(fake_token: CDEKToken) -> CDEKDeliveryPoint:
    return CDEKDeliveryPoint(token=fake_token)


@pytest.fixture()
def calculator(fake_token: CDEKToken) -> CDEKCalculator:
    return CDEKCalculator(token=fake_token)


@pytest.fixture()
def from_location() -> dict[str, Any]:
    """Митино"""
    return {"code": 468}


@pytest.fixture()
def to_location() -> dict[str, Any]:
    """Снежногорск"""
    return {"code": 2797}


@pytest.fixture()
def packages() -> list[dict[str, Any]]:
    return [
        {
            "height": 10,
            "length": 10,
            "width": 10,
            "weight": 4000,
        }
    ]
