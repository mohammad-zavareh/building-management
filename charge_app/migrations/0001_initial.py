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
            name='ServiceCharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='عنوان')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('amount', models.IntegerField(default=0, verbose_name='مبلغ')),
                ('divide_amount', models.CharField(choices=[('member', 'تقسیم بر تعداد ساکنین'), ('unit', 'تقسیم بر تعداد واحد ها')], max_length=30, verbose_name='تقسیم مبلغ')),
                ('expire_time', models.DateTimeField(verbose_name='تاریخ انقضا')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='building_app.building', verbose_name='برای ساختمان')),
                ('category', models.ManyToManyField(to='building_app.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'شارژ خدمات',
                'verbose_name_plural': 'شارژهای خدمات',
            },
        ),
        migrations.CreateModel(
            name='ServiceChargeStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='مبلغ قابل پرداخت واحد')),
                ('is_paid', models.BooleanField(default=False, verbose_name='پرداخت شده/نشده')),
                ('pay_time', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')),
                ('payment_type', models.CharField(blank=True, choices=[('online', 'آنلاین'), ('cash', 'نقدی')], max_length=10, null=True, verbose_name='نوع پرداخت')),
                ('service_charge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charge_app.servicecharge', verbose_name='شارژ خدمات')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='building_app.unit', verbose_name='واحد')),
            ],
            options={
                'verbose_name': 'وضعیت شارژ خدمات',
                'verbose_name_plural': 'وضعیت شارژهای خدمات',
            },
        ),
    ]
