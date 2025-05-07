from django.contrib import admin
from pages_app.models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {"fields": ("name",)},
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
    list_display = ("name",)
