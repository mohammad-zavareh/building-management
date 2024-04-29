# Generated by Django 4.1.2 on 2024-04-02 21:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('building_app', '0013_alter_building_image'),
        ('notification_app', '0004_notification_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='متن')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان ایجاد')),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification_app.notification', verbose_name='اعلان')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='building_app.unit', verbose_name='واحد')),
            ],
        ),
    ]