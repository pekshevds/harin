# Generated by Django 3.2.23 on 2024-02-16 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0007_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$YqH3t82cU91lQ5FOhnXce8$mKlYxyKCDu0d2+MZttP7NBOT94kASyS7Yate8u6ukmA=', max_length=128, verbose_name='password'),
        ),
    ]
