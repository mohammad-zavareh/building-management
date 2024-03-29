# Generated by Django 4.1.2 on 2023-05-19 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('building_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheba_number', models.CharField(max_length=30, verbose_name='شماره شبا')),
                ('amount', models.IntegerField(verbose_name='مبلغ')),
                ('paid', models.BooleanField(default=False, verbose_name='پرداخت شده/نشده')),
                ('pay_time', models.DateTimeField(blank=True, null=True, verbose_name='زمان پرداخت')),
                ('request_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان درخواست')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='building_app.building', verbose_name='ساختمان')),
            ],
            options={
                'verbose_name': 'درخواست پرداخت',
                'verbose_name_plural': 'درخواست های پرداخت',
            },
        ),
    ]
