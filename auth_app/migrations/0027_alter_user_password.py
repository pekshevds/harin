# Generated by Django 3.2.23 on 2025-02-17 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0026_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$uz25Pgq34spmJc0oucmsBj$LqRPorG81II9tX5KsFfw7wPPa32LvTjizFwjNV7i+Dw=', max_length=128, verbose_name='password'),
        ),
    ]
