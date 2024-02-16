# Generated by Django 3.2.23 on 2024-02-16 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='is_group',
            field=models.BooleanField(default=False, verbose_name='Это группа'),
        ),
        migrations.AddField(
            model_name='customer',
            name='is_group',
            field=models.BooleanField(default=False, verbose_name='Это группа'),
        ),
        migrations.AddField(
            model_name='organization',
            name='is_group',
            field=models.BooleanField(default=False, verbose_name='Это группа'),
        ),
    ]
