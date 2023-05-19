from django.db import models

from django.utils import timezone

from account_app.models import User
from building_management_app.models import Building,Unit


class RequestPayment(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name='ساختمان')
    sheba_number = models.CharField(max_length=30, verbose_name='شماره شبا')
    amount = models.IntegerField(verbose_name='مبلغ')
    paid = models.BooleanField(default=False, verbose_name='پرداخت شده/نشده')
    pay_time = models.DateTimeField(blank=True, null=True, verbose_name='زمان پرداخت')
    request_time = models.DateTimeField(auto_now_add=timezone.now,blank=True, null=True, verbose_name='زمان درخواست')

    def __str__(self):
        return f'شماره شبا {self.sheba_number}'

    class Meta:
        verbose_name = 'درخواست پرداخت'
        verbose_name_plural = 'درخواست های پرداخت'


class Notification(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name='برای ساختمان')
    title = models.CharField(max_length=50, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'اعلان'
        verbose_name_plural = 'اعلانات'
