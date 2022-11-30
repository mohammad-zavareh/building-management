# Generated by Django 4.1.2 on 2022-11-24 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_app', '0004_alter_requestpayment_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='building_id',
            field=models.CharField(default='eRzxr', max_length=5, unique=True, verbose_name='شناسه ساختمان'),
        ),
        migrations.AlterField(
            model_name='requestpayment',
            name='request_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان درخواست'),
        ),
    ]
