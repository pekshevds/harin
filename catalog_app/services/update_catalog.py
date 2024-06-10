from typing import List
from django.db import transaction
from catalog_app.models import (
    Good,
    Manufacturer,
    PriceKind,
    Price
)

goods = []
kind_prices = []
manufacturers = []
prices = []
parents = []


def find(_data, key) -> object | None:
    items = [item for item in _data if item.id == key]
    if items:
        return items[0]
    return None


def update_catalog_from_json(data: List) -> None:
    with transaction.atomic():
        for data_item in data:
            good = handle_good(data_item)
            for price_item in data_item['prices']:
                kind_price = handle_kind_prices(price_item)
                handle_price(price_item, good, kind_price)


def fill_good_fields(good, data) -> None:
    good.name = data['name']
    good.art = data['art']
    good.code = data['code']
    good.description = data['description']
    good.balance = data['balance']
    good.manufacturer = handle_manufacturer(data['manufacturer'])


def fill_kind_price_fields(kind_price, data) -> None:
    kind_price.name = data['name']


def handle_good(data) -> Good | None:
    if data:
        good = find(goods, data['id'])
        if not good:
            good, _ = Good.objects.get_or_create(id=data.get("id"))
            fill_good_fields(good, data)
            good.save()
            goods.append(good)
        return good


def handle_kind_prices(data) -> PriceKind | None:
    if data:
        kind_price = find(kind_prices, data['id'])
        if not kind_price:
            kind_price, _ = PriceKind.objects.get_or_create(id=data.get("id"))
            fill_kind_price_fields(kind_price, data)
            kind_price.save()
            kind_prices.append(kind_price)
        return kind_price


def handle_manufacturer(data) -> Manufacturer | None:
    if data:
        manufacturer = find(manufacturers, data.get("id"))
        if not manufacturer:
            manufacturer, _ = Manufacturer.objects.get_or_create(
                id=data.get("id"))
            fill_kind_price_fields(manufacturer, data)
            manufacturer.save()
            manufacturers.append(manufacturer)
        return manufacturer


def handle_price(data, good: Good, kind: PriceKind) -> Price | None:
    if data and good and kind:
        price, _ = Price.objects.get_or_create(good=good, kind=kind)
        price.price = data.get("price", 0)
        price.save()
        prices.append(price)
        return price
