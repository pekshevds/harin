# Generated by Django 3.2.23 on 2024-07-01 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0007_auto_20240610_1000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'ordering': ['good'], 'verbose_name': 'Запись', 'verbose_name_plural': 'Цены'},
        ),
        migrations.AddField(
            model_name='category',
            name='count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
