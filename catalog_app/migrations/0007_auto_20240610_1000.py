# Generated by Django 3.2.23 on 2024-06-10 07:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0006_auto_20240216_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='parent',
        ),
        migrations.AddField(
            model_name='good',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='good',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='goods', to='catalog_app.manufacturer', verbose_name='Производитель'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('name', models.CharField(blank=True, db_index=True, default='', max_length=150, null=True, verbose_name='Наименование')),
                ('is_group', models.BooleanField(default=False, verbose_name='Это группа')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='childs', to='catalog_app.category', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.AddField(
            model_name='good',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='goods', to='catalog_app.category', verbose_name='Категория'),
        ),
    ]
