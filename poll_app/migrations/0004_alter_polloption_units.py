# Generated by Django 4.1.2 on 2023-06-29 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_app', '0013_alter_building_image'),
        ('poll_app', '0003_remove_polloption_unit_polloption_units'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polloption',
            name='units',
            field=models.ManyToManyField(blank=True, null=True, related_name='votes', to='building_app.unit', verbose_name='رای دهندگان'),
        ),
    ]
