from django.db import models
from server.base import Directory


class Client(Directory):
    is_reseller = models.BooleanField(verbose_name="Это оптовик", default=False)
    inn = models.IntegerField(verbose_name="ИНН", blank=True, null=False, default=0)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
