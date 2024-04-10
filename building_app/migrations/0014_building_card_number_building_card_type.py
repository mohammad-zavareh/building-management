# Generated by Django 4.1.2 on 2024-04-09 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_app', '0013_alter_building_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='card_number',
            field=models.IntegerField(blank=True, max_length=16, null=True, verbose_name='شماره کارت'),
        ),
        migrations.AddField(
            model_name='building',
            name='card_type',
            field=models.CharField(blank=True, choices=[('saman', 'بانک سامان'), ('mellat', 'بانک ملت'), ('tejarat', 'بانک تجارت'), ('sepah', 'بانک سپه'), ('shahr', 'بانک شهر'), ('saderat', 'بانک صادرات'), ('keshavarzi', 'بانک کشاورزی')], max_length=50, null=True, verbose_name='نوع کارت'),
        ),
    ]
