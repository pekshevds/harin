# Generated by Django 3.2.23 on 2025-01-24 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0023_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$VGaj1cf9ORivY7pMr6JCNW$aPrOsCQGr5AcIeA8zmJ3bb+avmow5xG7gbJLM9AZcD0=', max_length=128, verbose_name='password'),
        ),
    ]
