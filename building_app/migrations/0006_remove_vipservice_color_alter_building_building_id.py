# Generated by Django 4.1.2 on 2022-11-28 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_app', '0005_alter_building_building_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vipservice',
            name='color',
        ),
        migrations.AlterField(
            model_name='building',
            name='building_id',
            field=models.CharField(default='opMEp', max_length=5, unique=True, verbose_name='شناسه ساختمان'),
        ),
    ]
