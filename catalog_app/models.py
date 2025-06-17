from django.db import models

# from pytils.translit import slugify
from django.db.models import QuerySet
from server.base import Base
from server.base import Directory
from image_app.models import Image

# from catalog_app.commons import secret_from_string
from const_app.commons import (
    fetch_seo_title_category,
    fetch_seo_description_category,
    fetch_seo_keywords_category,
    fetch_seo_title_good,
    fetch_seo_description_good,
    fetch_seo_keywords_good,
)

params: dict[str, str] = {
    "name": "name",
    "category": "category",
    "price1": "price",
    "art": "art",
}


class Manufacturer(Directory):
    count = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Category(Directory):
    code = models.CharField(
        verbose_name="Код", max_length=11, blank=True, null=False, default=""
    )
    parent = models.ForeignKey(
        "Category",
        verbose_name="Родитель",
        related_name="childs",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    count = models.IntegerField(null=True, blank=True, default=0)
    seo_title = models.TextField(
        verbose_name="<title>", null=True, blank=True, default=fetch_seo_title_category
    )
    seo_description = models.TextField(
        verbose_name="<description>",
        null=True,
        blank=True,
        default=fetch_seo_description_category,
    )
    seo_keywords = models.TextField(
        verbose_name="<keywords>",
        null=True,
        blank=True,
        default=fetch_seo_keywords_category,
    )

    @property
    def seo_cleaned_title(self):
        result = self.seo_title
        for key, value in params.items():
            result = result.replace(f"[{value}]", str(getattr(self, key, "")))
        return result

    @property
    def seo_cleaned_description(self):
        result = self.seo_description
        for key, value in params.items():
            result = result.replace(f"[{value}]", str(getattr(self, key, "")))
        return result

    @property
    def seo_cleaned_keywords(self):
        result = self.seo_keywords
        for key, value in params.items():
            result = result.replace(f"[{value}]", str(getattr(self, key, "")))
        return result

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Phrase(Directory):
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Фраза"
        verbose_name_plural = "Фразы для замены нулевого количества"


class Good(Directory):
    art = models.CharField(
        verbose_name="Артикул",
        max_length=50,
        blank=True,
        null=False,
        default="",
        db_index=True,
    )
    code = models.CharField(
        verbose_name="Код", max_length=11, blank=True, null=False, default=""
    )
    okei = models.CharField(
        verbose_name="Ед.", max_length=50, blank=True, null=False, default=""
    )
    balance = models.DecimalField(
        verbose_name="Остаток",
        max_digits=15,
        decimal_places=3,
        blank=True,
        null=True,
        default=0,
    )
    price1 = models.DecimalField(
        verbose_name="Розница магазин RUB",
        max_digits=15,
        decimal_places=2,
        blank=True,
        null=True,
        default=0,
    )
    price2 = models.DecimalField(
        verbose_name="Опт монтаж RUB",
        max_digits=15,
        decimal_places=2,
        blank=True,
        null=True,
        default=0,
    )
    price3 = models.DecimalField(
        verbose_name="Розница прайс RUB",
        max_digits=15,
        decimal_places=2,
        blank=True,
        null=True,
        default=0,
    )
    weight = models.DecimalField(
        verbose_name="Вес, кг",
        max_digits=15,
        decimal_places=3,
        blank=True,
        null=True,
        default=0,
    )
    length = models.DecimalField(
        verbose_name="Длина, м",
        max_digits=15,
        decimal_places=3,
        blank=True,
        null=True,
        default=0,
    )
    width = models.DecimalField(
        verbose_name="Ширина, м",
        max_digits=15,
        decimal_places=3,
        blank=True,
        null=True,
        default=0,
    )
    height = models.DecimalField(
        verbose_name="Высота, м",
        max_digits=15,
        decimal_places=3,
        blank=True,
        null=True,
        default=0,
    )
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    image = models.ForeignKey(
        Image,
        on_delete=models.PROTECT,
        verbose_name="Изображение (превью)",
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(verbose_name="Активен", default=True)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.PROTECT,
        verbose_name="Производитель",
        related_name="goods",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="Категория",
        related_name="goods",
        blank=True,
        null=True,
    )
    phrase = models.ForeignKey(
        Phrase,
        on_delete=models.PROTECT,
        verbose_name="Фраза для замены пустого количества",
        related_name="goods",
        blank=True,
        null=True,
    )
    description = models.CharField(
        verbose_name="Описание", max_length=2048, blank=True, null=False, default=""
    )
    seo_title = models.TextField(
        verbose_name="<title>", null=True, blank=True, default=fetch_seo_title_good
    )
    seo_description = models.TextField(
        verbose_name="<description>",
        null=True,
        blank=True,
        default=fetch_seo_description_good,
    )
    seo_keywords = models.TextField(
        verbose_name="<keywords>",
        null=True,
        blank=True,
        default=fetch_seo_keywords_good,
    )

    @property
    def seo_cleaned_title(self):
        result = self.seo_title
        for key, value in params.items():
            result = result.replace(f"[{value}]", str(getattr(self, key, "")))
        return result

    @property
    def seo_cleaned_description(self):
        result = self.seo_description
        for key, value in params.items():
            result = result.replace(f"[{value}]", str(getattr(self, key, "")))
        return result

    @property
    def seo_cleaned_keywords(self):
        result = self.seo_keywords
        for key, value in params.items():
            result = result.replace(f"[{value}]", str(getattr(self, key, "")))
        return result

    @property
    def description_html(self):
        description = ""
        for line in self.description.split("\n"):
            description += f"<p>{line}</p>"
        return description

    def save(self, *args, **kwargs) -> None:
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class PriceKind(Directory):
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Вид цены"
        verbose_name_plural = "Виды цен"


class Price(Base):
    good = models.ForeignKey(
        Good, on_delete=models.PROTECT, verbose_name="Номенклатура"
    )
    kind = models.ForeignKey(
        PriceKind, on_delete=models.PROTECT, verbose_name="Вид цены"
    )
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=15,
        decimal_places=2,
        blank=True,
        null=True,
        default=0,
    )

    def __str__(self) -> str:
        return f"{self.good}-{self.kind}"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Цены"
        ordering = [
            "good",
        ]


class GoodsImage(Base):
    good = models.ForeignKey(
        Good,
        on_delete=models.PROTECT,
        verbose_name="Номенклатура",
        related_name="images",
    )
    image = models.ForeignKey(
        Image, on_delete=models.PROTECT, verbose_name="Изображение"
    )

    def __str__(self) -> str:
        return self.image.name

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения товара"
