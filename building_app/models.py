from django.db import models

from django.utils import timezone

from account_app.models import User
from vip_service_app.models import VipService


class Building(models.Model):
    manager = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='مدیر')
    name = models.CharField(max_length=20, verbose_name='نام')
    image = models.ImageField(upload_to='building',null=True,blank=True, verbose_name='تصویر')
    rules = models.TextField(blank=True, null=True, verbose_name='قوانین')
    credit = models.IntegerField(default=0, verbose_name='کیف پول')
    vip_plan = models.ForeignKey(VipService, on_delete=models.CASCADE, verbose_name='اشتراک ویژه',
                                 related_name='building',
                                 blank=True, null=True)
    vip_time = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انقضا اشتراک')
    max_unit = models.CharField(choices=VipService.MAX_UNIT_CHOICE, max_length=50, verbose_name='حداکثر واحد')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ساختمان'
        verbose_name_plural = 'ساختمان ها'

    def is_vip(self):
        if self.vip_time > timezone.now():
            return True
        elif self.vip_time < timezone.now():
            return False
        else:
            return False

    is_vip.boolean = True
    is_vip.short_description = 'دارای اشتراک'

    def until_vip_time(self):
        until_time = self.vip_time - timezone.now()
        return until_time.days


class Unit(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name='برای ساختمان')
    resident = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='ساکن')

    name = models.CharField(max_length=50, verbose_name='نام')
    number_of_member = models.IntegerField(default=1, verbose_name='تعداد ساکنین')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'واحد'
        verbose_name_plural = 'واحد ها'
