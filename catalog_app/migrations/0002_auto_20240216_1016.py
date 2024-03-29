# Generated by Django 3.2.23 on 2024-02-16 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='good',
            old_name='price',
            new_name='price1',
        ),
        migrations.RemoveField(
            model_name='good',
            name='category',
        ),
        migrations.AddField(
            model_name='good',
            name='code',
            field=models.CharField(blank=True, default='', max_length=11, null=True, verbose_name='Код'),
        ),
        migrations.AddField(
            model_name='good',
            name='description',
            field=models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='good',
            name='is_group',
            field=models.BooleanField(default=False, verbose_name='Это группа'),
        ),
        migrations.AddField(
            model_name='good',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='goods', to='catalog_app.good', verbose_name='Родитель'),
        ),
        migrations.AddField(
            model_name='good',
            name='price2',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='is_group',
            field=models.BooleanField(default=False, verbose_name='Это группа'),
        ),
        migrations.DeleteModel(
            name='Applicability',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Model',
        ),
    ]
