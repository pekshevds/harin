# Generated by Django 3.2.23 on 2025-04-16 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0035_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$7rwfANnl5SdXOykQmYnuig$CA/Js0GvbV2j+ZFn9eHcc+V8HIuspdh7+S4/vhQTvuc=', max_length=128, verbose_name='password'),
        ),
    ]
