# Generated by Django 3.2.23 on 2025-04-16 04:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0017_auto_20250414_0657'),
    ]

    operations = [
        migrations.CreateModel(
            name='SEODefaults',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('seo_title_category', models.TextField(blank=True, default='', null=True, verbose_name='<title>')),
                ('seo_description_category', models.TextField(blank=True, default='', null=True, verbose_name='<description>')),
                ('seo_keywords_category', models.TextField(blank=True, default='', null=True, verbose_name='<keywords>')),
                ('seo_title_good', models.TextField(blank=True, default='', null=True, verbose_name='<title>')),
                ('seo_description_good', models.TextField(blank=True, default='', null=True, verbose_name='<description>')),
                ('seo_keywords_good', models.TextField(blank=True, default='', null=True, verbose_name='<keywords>')),
            ],
            options={
                'verbose_name': 'Шаблон SEO',
                'verbose_name_plural': 'Шаблоны SEO',
            },
        ),
    ]
