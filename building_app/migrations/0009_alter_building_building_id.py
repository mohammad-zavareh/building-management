# Generated by Django 4.1.2 on 2023-06-16 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_app', '0008_alter_building_building_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='building_id',
            field=models.CharField(default='aiJmE', max_length=5, unique=True, verbose_name='شناسه ساختمان'),
        ),
    ]
