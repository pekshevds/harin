# Generated by Django 3.2.23 on 2024-02-16 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0005_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$rcy3NPr5bO6a3PkOqqfuEy$Ns/w9b07/mNwgyPuhUiaL2+Vfy/P2ogFzbrmGGdNz2w=', max_length=128, verbose_name='password'),
        ),
    ]