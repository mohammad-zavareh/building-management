# Generated by Django 4.1.2 on 2022-11-24 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_app', '0003_alter_building_building_id_requestpayment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requestpayment',
            options={'verbose_name': 'درخواست پرداخت', 'verbose_name_plural': 'درخواست های پرداخت'},
        ),
        migrations.AlterField(
            model_name='building',
            name='building_id',
            field=models.CharField(default='9FX5T', max_length=5, unique=True, verbose_name='شناسه ساختمان'),
        ),
        migrations.AlterField(
            model_name='requestpayment',
            name='sheba_number',
            field=models.CharField(max_length=30, verbose_name='شماره شبا'),
        ),
    ]
