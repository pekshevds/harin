from django.utils.html import format_html
from django.contrib import admin
from catalog_app.models import (
    Good,
    GoodsImage,
    Manufacturer
)

admin.site.site_header = 'Панель администрирования harin'
admin.site.site_title = 'Панель администрирования harin'
admin.site.index_title = 'Добро пожаловать!'


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id',)


class GoodsImageInLine(admin.TabularInline):
    model = GoodsImage
    fields = ('image', 'preview',)
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            str = f"<img src={obj.image.image.url} style='max-height: 75px;'>"
            return format_html(str)


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'art',
        'is_active', 'balance', 'price1', 'price2', 'preview',
    )
    search_fields = ('name', 'art',)

    def preview(self, obj):
        if obj.image:
            str = f"<img src={obj.image.image.url} style='max-height: 75px;'>"
            return format_html(str)

    preview.short_description = 'Изображение (превью)'
