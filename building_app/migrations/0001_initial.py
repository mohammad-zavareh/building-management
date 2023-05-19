# Generated by Django 4.1.2 on 2023-05-19 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vip_service_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_id', models.CharField(default='0aHOg', max_length=5, unique=True, verbose_name='شناسه ساختمان')),
                ('name', models.CharField(max_length=20, verbose_name='نام')),
                ('image', models.ImageField(upload_to='building', verbose_name='تصویر')),
                ('rules', models.TextField(blank=True, null=True, verbose_name='قوانین')),
                ('credit', models.IntegerField(default=0, verbose_name='کیف پول')),
                ('vip_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انقضا اشتراک')),
                ('vip_plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='building', to='vip_service_app.vipservice', verbose_name='اشتراک ویژه')),
            ],
            options={
                'verbose_name': 'ساختمان',
                'verbose_name_plural': 'ساختمان ها',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='عنوان')),
                ('is_active', models.BooleanField(verbose_name='فعال/غیرفعال')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('is_manager', models.BooleanField(default=False, verbose_name='مدیر ساختمان')),
                ('number_of_member', models.IntegerField(default=1, verbose_name='تعداد ساکنین')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='building_app.building', verbose_name='برای ساختمان')),
                ('resident', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ساکن')),
            ],
            options={
                'verbose_name': 'واحد',
                'verbose_name_plural': 'واحد ها',
            },
        ),
    ]