# Generated by Django 3.2.23 on 2024-02-16 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0004_auto_20240216_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='slug',
        ),
    ]
