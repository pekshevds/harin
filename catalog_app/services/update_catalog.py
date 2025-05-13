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
    category.code = data_item.get("code", category.code)
    category.parent = handle_parent(data_item.get("parent"))
    category.save()
    return category


def _fetch_required_fields() -> list[str]:
    fields = []
    fields.append("name")
    fields.append("code")
    fields.append("okei")
    fields.append("art")
    fields.append("description")
    fields.append("balance")
    fields.append("price1")
    fields.append("price2")
    fields.append("price3")
    fields.append("weight")
    fields.append("length")
    fields.append("width")
    fields.append("height")
    return fields


def handle_good(data_item: dict[Any, Any] | None) -> Good | None:
    if data_item is None:
        return None
    good, _ = Good.objects.get_or_create(id=data_item.get("id"))
    for field in _fetch_required_fields():
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
