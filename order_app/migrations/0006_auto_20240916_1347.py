# Generated by Django 3.2.23 on 2024-09-16 10:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0005_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='number',
            field=models.CharField(blank=True, default='', max_length=25, verbose_name='Номер'),
        ),
    ]
