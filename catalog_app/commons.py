import hashlib
from django.http import HttpRequest
from django.db.models import Q
from django.db.models import QuerySet
from catalog_app.services.manufacturer import manufacturer_by_id_list
from catalog_app.services.category import category_by_id_list
from catalog_app.models import Good
from catalog_app.models import Category as CategoryModel
from yml_catalog import YmlCatalog, Category, Offer
from django.conf import settings
from const_app.commons import fetch_current_consts
from catalog_app.services.good import active_items, fetch_goods_queryset_by_filters


def fill_seo_category_defaults() -> None:
    current_consts = fetch_current_consts()
    if current_consts:
        CategoryModel.objects.all().update(
            seo_title=current_consts.seo_title_category,
            seo_description=current_consts.seo_description_category,
            seo_keywords=current_consts.seo_keywords_category,
        )


def fill_seo_good_defaults() -> None:
    current_consts = fetch_current_consts()
    if current_consts:
        Good.objects.all().update(
            seo_title=current_consts.seo_title_good,
            seo_description=current_consts.seo_description_good,
            seo_keywords=current_consts.seo_keywords_good,
        )


def fill_seo_defaults() -> None:
    fill_seo_category_defaults()
    fill_seo_good_defaults()


def update_yml_catalog_xml() -> None:
    yml_catalog = YmlCatalog(
        "catalog", "magazin-poliva1", settings.FRONTEND_DOMAIN, "site"
    )
    queryset = active_items()
    categories = []
    offers = []
    for good in queryset:
        offers.append(
            Offer(
                id=clean_code(good.code),
                categoryId=clean_code(good.category.code) if good.category else "",
                name=good.name,
                url=f"{settings.FRONTEND_DOMAIN}/catalog/good/{str(good.id)}/",
                price=str(int(good.price1)),
                oldprice=str(int(good.price3)),
                currencyId="RUB",
                delivery="true",
                pickup="true",
                store="false",
                description=f"{good.description}",
                model=good.name,
                vendor=good.manufacturer.name if good.manufacturer else "",
                vendorCode=good.art,
                picture=f"{settings.BACKEND_DOMAIN}{good.image.image.url}"
                if good.image
                else "",
                available="true" if good.balance > 0 else "false",
            )
        )
        if good.category:
            category = Category(
                clean_code(good.category.code),
                clean_code(good.category.parent.code) if good.category.parent else "",
                good.category.name,
            )
            if category not in categories:
                categories.append(category)
    yml_catalog.load_categories(categories)
    yml_catalog.load_offers(offers)
    yml_catalog.save_to_file(settings.MEDIA_ROOT / "yml_catalog.xml")


def clean_code(code: str) -> str:
    words = code.split("-")
    if len(words) == 2:
        right = words[1]
        try:
            int_code = int(right)
        except ValueError:
            return code
        return str(int_code)
    else:
        try:
            int_code = int(code)
        except ValueError:
            return code
        return str(int_code)


def secret_from_string(string: str) -> str:
    hash = hashlib.blake2s(digest_size=4)
    hash.update(string.encode("utf-8"))
    return hash.hexdigest()


def fetch_filters(request: HttpRequest) -> list:
    categories = None
    obj_id = request.GET.get("category_id")
    if obj_id:
        categories = category_by_id_list(obj_id.split(","))

    manufacturers = None
    obj_id = request.GET.get("manufacturer_id")
    if obj_id:
        manufacturers = manufacturer_by_id_list(obj_id.split(","))

    return [categories, manufacturers]


def fetch_goods_by_filters(args) -> QuerySet:
    queryset = fetch_goods_queryset_by_filters(args[0], args[1])
    return queryset
