# Generated by Django 3.2.23 on 2025-02-18 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0006_auto_20240916_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='uploaded_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата загрузки в 1С'),
        ),
    ]
