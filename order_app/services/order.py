from django.db import transaction
from django.db.models import QuerySet
from order_app.models import Order, ItemOrder
from auth_app.models import User
from catalog_app.services.good import good_by_id


def order_by_id(order_id: str) -> Order:
    return Order.objects.filter(id=order_id).first()


def item_order_by_id(item_order_id: str) -> ItemOrder:
    return ItemOrder.objects.filter(id=item_order_id).first()


def handle_order(order_dict: dict, author: None | User) -> Order:
    changed = False
    order_id = order_dict.get("id", None)
    order, _ = Order.objects.get_or_create(id=order_id)
    if _:
        order.author = author
        order.client = author.client if author else None
        changed = True
    key_name = "items"
    if key_name in order_dict:
        items = order_dict.get(key_name, [])
        handle_items_order(items, order=order)
    if changed:
        order.save()
    return order


def handle_items_order(items_list: list, order: Order) -> None:
    changed = False
    for item_dir in items_list:
        item_order_id = item_dir.get("id", None)
        item_order, _ = ItemOrder.objects.get_or_create(id=item_order_id, order=order)
        if _:
            changed = True

        key_name = "good_id"
        if key_name in item_dir:
            good_id = item_dir.get(key_name)
            item_order.good = None if good_id is None else good_by_id(good_id=good_id)
            changed = True

        key_name = "quantity"
        if key_name in item_dir:
            setattr(item_order, key_name, item_dir.get(key_name))
            changed = True

        key_name = "price"
        if key_name in item_dir:
            setattr(item_order, key_name, item_dir.get(key_name))
            changed = True

        key_name = "summ"
        if key_name in item_dir:
            setattr(item_order, key_name, item_dir.get(key_name))
            changed = True
        if changed:
            item_order.save()


def handle_order_list(order_list: list[dict], author: User) -> QuerySet:
    orders_id = []
    with transaction.atomic():
        for order_item in order_list:
            order = handle_order(order_dict=order_item, author=author)
            orders_id.append(order.id)
    return Order.objects.filter(id__in=orders_id)
