# Generated by Django 3.2.23 on 2024-08-29 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0013_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$5PZAgpzal7nkr2gt2HhiQ3$3fcUPJWK9RUOrXKmHeWjMOeQg1jDXRLqp49V9irgulQ=', max_length=128, verbose_name='password'),
        ),
    ]
