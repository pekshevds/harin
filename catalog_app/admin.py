from django.utils.html import format_html
from django.contrib import admin
from catalog_app.models import (
    Category,
    Good,
    GoodsImage,
    Manufacturer,
    PriceKind,
    Price
)

admin.site.site_header = "Панель администрирования harin"
admin.site.site_title = "Панель администрирования harin"
admin.site.index_title = "Добро пожаловать!"


@admin.register(Category)
class CategoryKindAdmin(admin.ModelAdmin):
    list_display = ("__str__", "id", "parent")


@admin.register(PriceKind)
class PriceKindAdmin(admin.ModelAdmin):
    list_display = ("__str__", "id",)


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ("__str__", "price", "id",)
    exclude = ("name",)
    list_filter = ("kind",)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("__str__", "id",)


class PriceInLine(admin.TabularInline):
    model = Price
    fields = ("kind", "price",)


class GoodsImageInLine(admin.TabularInline):
    model = GoodsImage
    fields = ("image", "preview",)
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.image:
            str = f"<img src={obj.image.image.url} style='max-height: 75px;'>"
            return format_html(str)


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    inlines = [PriceInLine,]
    list_display = (
        "name", "art",
        "is_active", "balance", "preview", "category", "manufacturer",
    )
    search_fields = ("name", "art",)
    list_filter = ("manufacturer", "category",)

    def preview(self, obj):
        if obj.image:
            str = f"<img src={obj.image.image.url} style='max-height: 75px;'>"
            return format_html(str)

    preview.short_description = "Изображение (превью)"
