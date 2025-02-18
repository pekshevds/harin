from django.db import models
from django.utils.translation import gettext_lazy as _
from server.base import Directory


class Recipient(Directory):
    email = models.EmailField(_("email address"), blank=False, unique=True)

    class Meta:
        verbose_name = "Получатель"
        verbose_name_plural = "Получатели"
