# Generated by Django 4.1.2 on 2023-06-25 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_app', '0011_remove_building_building_id_building_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='max_unit',
            field=models.CharField(choices=[('10', 'کمتر از 10 واحد'), ('30', '11 تا 30 واحد'), ('50', '31 تا 50 واحد'), ('100', '51 تا 100 واحد'), ('300', '100 تا 300 واحد'), ('500', '300 تا 500 واحد'), ('5000', 'بیشتر از 500 واحد')], default=1, max_length=50, verbose_name='حداکثر واحد'),
            preserve_default=False,
        ),
    ]