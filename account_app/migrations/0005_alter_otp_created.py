# Generated by Django 4.1.2 on 2023-05-13 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0004_alter_otp_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
