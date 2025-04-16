from django.db import models
from server.base import Base


class SEODefaults(Base):
    seo_title_category = models.TextField(
        verbose_name="<title>", null=True, blank=True, default=""
    )
    seo_description_category = models.TextField(
        verbose_name="<description>",
        null=True,
        blank=True,
        default="",
    )
    seo_keywords_category = models.TextField(
        verbose_name="<keywords>",
        null=True,
        blank=True,
        default="",
    )
    seo_title_good = models.TextField(
        verbose_name="<title>", null=True, blank=True, default=""
    )
    seo_description_good = models.TextField(
        verbose_name="<description>",
        null=True,
        blank=True,
        default="",
    )
    seo_keywords_good = models.TextField(
        verbose_name="<keywords>",
        null=True,
        blank=True,
        default="",
    )

    class Meta:
        verbose_name = "Шаблон SEO"
        verbose_name_plural = "Шаблоны SEO"
