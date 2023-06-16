# Generated by Django 4.1.2 on 2023-06-16 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('building_app', '0010_remove_unit_is_manager_alter_building_building_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='building_id',
        ),
        migrations.AddField(
            model_name='building',
            name='manager',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='مدیر'),
            preserve_default=False,
        ),
    ]
