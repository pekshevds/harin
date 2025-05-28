from django.db import transaction
from django.db.models import QuerySet
from order_app.models import Order, ItemOrder
from django.template.loader import render_to_string
from auth_app.models import User
from catalog_app.services.good import good_by_id
from auth_app.transport import send_mail


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
        order.comment = f"{order_dict.get('name', '')}, {order_dict.get('email', '')}, {order_dict.get('phone', '')}"
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


def prepare_order_items(items: list[dict]) -> None:
    for index, item in enumerate(items, start=1):
        good = good_by_id(good_id=item["good_id"])
        item["index"] = index
        item["art"] = good.art if good else ""
        item["name"] = good.name if good else ""


def send_order_list_from_rain_block_ru(order_list: list[dict]) -> None:
    for order_item in order_list:
        prepare_order_items(order_item["items"])
        subject = "Новый заказ"
        message = "Новый заказ"
        recipient_list = [order_item["email"], "89205772244@mail.ru"]
        html_message = render_to_string(
            "order_app/html_message.html", context=order_item
        )
        send_mail(subject, message, recipient_list, html_message)
