# Generated by Django 4.1.2 on 2023-06-16 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0006_user_is_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_manager',
            field=models.BooleanField(default=False, verbose_name='مدیر ساختمان'),
        ),
    ]
