# Generated by Django 3.2.23 on 2025-01-20 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0011_auto_20240912_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='price3',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='Розница прайс RUB'),
        ),
        migrations.AlterField(
            model_name='good',
            name='price1',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='Розница магазин RUB'),
        ),
        migrations.AlterField(
            model_name='good',
            name='price2',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='Опт монтаж RUB'),
        ),
    ]
