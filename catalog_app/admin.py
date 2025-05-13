from django.utils.html import format_html
from django.contrib import admin
from catalog_app.models import (
    Category,
    Good,
    GoodsImage,
    Manufacturer,
    Phrase,
    # PriceKind,
    # Price,
)
from const_app.commons import fetch_current_consts

admin.site.site_header = "Панель администрирования harin"
admin.site.site_title = "Панель администрирования harin"
admin.site.index_title = "Добро пожаловать!"


@admin.action(description="Заполнить SEO по умолчанию")
def fill_seo_category_defaults(modeladmin, request, queryset):
    current_consts = fetch_current_consts()
    if current_consts:
        queryset.update(
            seo_title=current_consts.seo_title_category,
            seo_description=current_consts.seo_description_category,
            seo_keywords=current_consts.seo_keywords_category,
        )


@admin.register(Category)
class CategoryKindAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "parent",
                    "code",
                    "comment",
                )
            },
        ),
        (
            "CEO",
            {
                "fields": (
                    (
                        "seo_title",
                        "seo_description",
                        "seo_keywords",
                    )
                )
            },
        ),
    )
    list_display = (
        "__str__",
        "id",
        "parent",
        "code",
    )
    actions = [fill_seo_category_defaults]


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "id",
    )


@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "id",
    )


class GoodsImageInLine(admin.TabularInline):
    model = GoodsImage
    fields = (
        "image",
        "preview",
    )
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.image:
            str = f"<img src={obj.image.image.url} style='max-height: 75px;'>"
            return format_html(str)


@admin.action(description="Заполнить SEO по умолчанию")
def fill_seo_good_defaults(modeladmin, request, queryset):
    current_consts = fetch_current_consts()
    if current_consts:
        queryset.update(
            seo_title=current_consts.seo_title_good,
            seo_description=current_consts.seo_description_good,
            seo_keywords=current_consts.seo_keywords_good,
        )


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    (
                        "art",
                        "code",
                        "okei",
                    ),
                    "is_active",
                )
            },
        ),
        (
            "Цены",
            {
                "fields": (
                    (
                        "price1",
                        "price2",
                        "price3",
                    )
                )
            },
        ),
        (
            None,
            {
                "fields": (
                    (
                        "balance",
                        "phrase",
                    ),
                    "category",
                    "manufacturer",
                    (
                        "image",
                        "preview",
                    ),
                    "description",
                    "comment",
                )
            },
        ),
        (
            "Физические параметры",
            {
                "fields": (
                    (
                        "weight",
                        "length",
                        "width",
                        "height",
                    )
                )
            },
        ),
        (
            "CEO",
            {
                "fields": (
                    (
                        "seo_title",
                        "seo_description",
                        "seo_keywords",
                    )
                )
            },
        ),
    )

    list_display = (
        "name",
        "art",
        "code",
        "okei",
        "is_active",
        "balance",
        "price1",
        "price2",
        "price3",
        "preview",
        "category",
        "manufacturer",
    )
    search_fields = (
        "name",
        "art",
    )
    list_filter = (
        "manufacturer",
        "category",
    )
    readonly_fields = ("preview",)

    actions = [fill_seo_good_defaults]

    def preview(self, obj):
        if obj.image:
            str = f"'<img src={obj.image.image.url} style='max-height: 75px;'>"
            return format_html(str)
        return ""

    preview.short_description = "Изображение (превью)"
