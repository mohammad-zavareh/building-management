# Generated by Django 4.1.2 on 2023-05-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_app', '0002_alter_building_building_id'),
        ('notification_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='hits',
            field=models.ManyToManyField(to='building_app.unit', verbose_name='بازدید'),
        ),
    ]
