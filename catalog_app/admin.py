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

admin.site.site_header = "Панель администрирования harin"
admin.site.site_title = "Панель администрирования harin"
admin.site.index_title = "Добро пожаловать!"


@admin.register(Category)
class CategoryKindAdmin(admin.ModelAdmin):
    list_display = ("__str__", "id", "parent")


"""@admin.register(PriceKind)
class PriceKindAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "id",
    )"""


"""@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "price",
        "id",
    )
    exclude = ("name",)
    list_filter = ("kind",)"""


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


"""class PriceInLine(admin.TabularInline):
    model = Price
    fields = (
        "kind",
        "price",
    )"""


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
    )

    list_display = (
        "name",
        "art",
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

    def preview(self, obj):
        if obj.image:
            str = f"'<img src={obj.image.image.url} style='max-height: 75px;'>"
            return format_html(str)
        return ""

    preview.short_description = "Изображение (превью)"
