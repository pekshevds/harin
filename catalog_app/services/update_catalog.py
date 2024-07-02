from typing import Any
from django.db import transaction
from catalog_app.models import Good, PriceKind, Price, Category


def handle_price_kind(data_item: dict | None) -> PriceKind | None:
    if data_item is None:
        return None
    price_kind, _ = PriceKind.objects.get_or_create(id=data_item.get("id"))
    price_kind.name = data_item.get("name", price_kind.name)
    price_kind.save()
    return price_kind


def handle_prices(good: Good, data: list[dict[str, Any]] | None) -> None:
    if data is None:
        return
    for data_item in data:
        price_kind = handle_price_kind(data_item)
        price, _ = Price.objects.get_or_create(kind=price_kind, good=good)
        price.price = data_item.get("price", price.price)
        price.save()


def handle_parent(data_item: dict[Any, Any] | None) -> Category | None:
    if data_item is None:
        return None
    category, _ = Category.objects.get_or_create(id=data_item.get("id"))
    category.name = data_item.get("name", category.name)
    category.parent = handle_parent(data_item.get("parent"))
    category.save()
    return category


def handle_good(data_item: dict[Any, Any] | None) -> Good | None:
    if data_item is None:
        return None
    good, _ = Good.objects.get_or_create(id=data_item.get("id"))
    for field in "name,code,art,description,balance".split(","):
        setattr(good, field, data_item.get(field, getattr(good, field)))
    good.category = handle_parent(data_item.get("parent"))
    good.save()
    return good


def update_catalog_from_json(data: list[dict]) -> None:
    with transaction.atomic():
        for data_item in data:
            good = handle_good(data_item)
            if good:
                handle_prices(good, data_item.get("prices"))
