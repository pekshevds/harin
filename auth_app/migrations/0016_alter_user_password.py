# Generated by Django 3.2.23 on 2024-09-05 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0015_auto_20240830_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$x6M9wnFnLBlqaxZqTu7ESw$ypBGijaGTRbxdnuMz8aMpb/e1FR86bw/OWY0LLo4qcU=', max_length=128, verbose_name='password'),
        ),
    ]
