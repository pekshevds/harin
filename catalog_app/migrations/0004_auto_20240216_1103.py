# Generated by Django 3.2.23 on 2024-02-16 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0003_auto_20240216_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricekind',
            name='is_group',
            field=models.BooleanField(default=False, verbose_name='Это группа'),
        ),
        migrations.AddField(
            model_name='pricekind',
            name='name',
            field=models.CharField(blank=True, db_index=True, max_length=150, null=True, verbose_name='Наименование'),
        ),
    ]