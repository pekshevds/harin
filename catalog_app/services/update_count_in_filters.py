from dataclasses import dataclass
from django.db.models import QuerySet
from catalog_app.models import Category, Manufacturer


@dataclass
class Data:
    def __init__(self, manufacturer: QuerySet, category: QuerySet) -> None:
        self.manufacturer = manufacturer
        self.category = category


def update_count_in_filter(_class):
    obj_for_update = []
    for obj in _class.objects.all():
        obj.count = obj.goods.count()
        obj_for_update.append(obj)
    _class.objects.bulk_update(obj_for_update, ["count"], batch_size=100)


def update_count_in_filters():
    update_count_in_filter(Category)
    update_count_in_filter(Manufacturer)


def fetch_filters_by_goods() -> Data:
    return Data(
        manufacturer=Manufacturer.objects.filter(count__gt=0).order_by("-count"),
        category=Category.objects.filter(count__gt=0).order_by("-count"),
    )
