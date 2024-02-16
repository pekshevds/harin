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
    good.id = data['id']
    good.name = data['name']
    good.art = data['art']
    good.code = data['code']
    good.description = data['description']
    good.balance = data['balance']
    good.manufacturer = handle_manufacturer(data['manufacturer'])
    good.parent = handle_parent(data['parent'])


def fill_parent_fields(good, data) -> None:
    good.id = data['id']
    good.name = data['name']
    good.code = data['code']
    good.is_group = True
    good.parent = handle_parent(data['parent'])


def fill_kind_price_fields(kind_price, data) -> None:
    kind_price.id = data['id']
    kind_price.name = data['name']


def handle_good(data) -> Good | None:
    if data:
        good = find(goods, data['id'])
        if not good:
            good = Good.objects.filter(id=data['id']).first()
            if not good:
                good = Good()
            fill_good_fields(good, data)
            good.save()
            goods.append(good)
        return good


def handle_kind_prices(data) -> PriceKind | None:
    if data:
        kind_price = find(kind_prices, data['id'])
        if not kind_price:
            kind_price = PriceKind.objects.filter(id=data['id']).first()
            if not kind_price:
                kind_price = PriceKind()
            fill_kind_price_fields(kind_price, data)
            kind_price.save()
            kind_prices.append(kind_price)
        return kind_price


def handle_manufacturer(data) -> Manufacturer | None:
    if data:
        manufacturer = find(manufacturers, data['id'])
        if not manufacturer:
            manufacturer = Manufacturer.objects.filter(id=data['id']).first()
            if not manufacturer:
                manufacturer = Manufacturer()
            fill_kind_price_fields(manufacturer, data)
            manufacturer.save()
            manufacturers.append(manufacturer)
        return manufacturer


def handle_price(data, good: Good, kind: PriceKind) -> Price | None:
    if data and good and kind:
        price = Price.objects.filter(good=good, kind=kind).first()
        if not price:
            price = Price(good=good, kind=kind)
        price.price = data['price']
        price.save()
        prices.append(price)
        return price


def handle_parent(data) -> Good | None:
    if data:
        parent = Good.objects.filter(id=data['id']).first()
        if not parent:
            parent = Good()
        fill_parent_fields(parent, data)
        parent.parent = handle_parent(data['parent'])
        parent.save()
        parents.append(parent)
        return parent
