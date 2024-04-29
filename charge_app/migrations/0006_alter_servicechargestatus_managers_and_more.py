# Generated by Django 4.1.2 on 2024-04-08 22:12

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('charge_app', '0005_remove_servicecharge_category_servicecharge_category'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='servicechargestatus',
            managers=[
                ('status_by_paid', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='servicechargestatus',
            name='is_paid',
        ),
        migrations.AddField(
            model_name='servicechargestatus',
            name='status',
            field=models.CharField(choices=[('online_paid', 'پرداخت نشده - آنلاین'), ('offline_paid', 'پرداخت شده - آفلاین'), ('unpaid', 'پرداخت نشده'), ('unpaid_waiting', 'پرداخت نشده - در انتظار بررسی'), ('unpaid_reject', 'پرداخت نشده - رد شده')], default='unpaid', max_length=50, verbose_name='وضعیت پرداخت'),
        ),
    ]