from django.contrib import admin
from const_app.models import SEODefaults


@admin.register(SEODefaults)
class SEODefaultsAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Товары",
            {
                "fields": (
                    "seo_title_good",
                    "seo_description_good",
                    "seo_keywords_good",
                )
            },
        ),
        (
            "Категории",
            {
                "fields": (
                    "seo_title_category",
                    "seo_description_category",
                    "seo_keywords_category",
                )
            },
        ),
        (
            None,
            {"fields": ("comment",)},
        ),
    )
    list_display = (
        "id",
        "created_at",
        "updated_at",
    )
