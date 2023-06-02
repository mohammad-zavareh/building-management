from django.db import models

from django.db.models.signals import post_save

from django.dispatch import receiver
from django.utils import timezone

from account_app.models import User
from vip_service_app.models import VipService
from building_app.models import Building, Unit, Category


class ServiceCharge(models.Model):  # divide_members   divide_units
    divide_type = [
        ('member', 'تقسیم بر تعداد ساکنین'),
        ('unit', 'تقسیم بر تعداد واحد ها')
    ]

    building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name='برای ساختمان')
    title = models.CharField(max_length=30, verbose_name='عنوان')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')
    amount = models.IntegerField(default=0, verbose_name='مبلغ')
    divide_amount = models.CharField(max_length=30, choices=divide_type, verbose_name='تقسیم مبلغ')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی')
    expire_time = models.DateTimeField(verbose_name='تاریخ انقضا')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'شارژ خدمات'
        verbose_name_plural = 'شارژهای خدمات'

    def is_active(self):
        expire_time = self.expire_time

        if expire_time < timezone.now():
            return False
        elif expire_time > timezone.now():
            return True

    is_active.boolean = True
    is_active.short_description = 'فعال'

    def get_categories(self):
        return " ,".join([i.title for i in self.category.all()])

    get_categories.short_description = 'دسته بندی'


class ServiceChargeStatus(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name='واحد')
    service_charge = models.ForeignKey(ServiceCharge, on_delete=models.CASCADE, verbose_name='شارژ خدمات')

    amount = models.IntegerField(verbose_name='مبلغ قابل پرداخت واحد')
    is_paid = models.BooleanField(default=False, verbose_name='پرداخت شده/نشده')
    pay_time = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')


    def __str__(self):
        return f'{self.service_charge} => {self.unit}'

    class Meta:
        verbose_name = 'وضعیت شارژ خدمات'
        verbose_name_plural = 'وضعیت شارژهای خدمات'


# signal for create ServiceChargeStatus object

@receiver(post_save, sender=ServiceCharge)
def create_service_charge_status(sender, instance, created, **kwargs):
    if created:  # if false is mean: update
        service_charge = instance
        building = instance.building
        units = Unit.objects.filter(building=building)

        number_of_building_member = sum([unit.number_of_member for unit in units])

        amount_member = service_charge.amount / number_of_building_member
        amount_unit = service_charge.amount / len(units)

        divide_type = service_charge.divide_amount

        if divide_type == 'member':
            for unit in units:
                amount_unit = amount_member * unit.number_of_member
                ServiceChargeStatus.objects.create(unit=unit, service_charge=service_charge, amount=amount_unit)
        elif divide_type == 'unit':
            for unit in units:
                ServiceChargeStatus.objects.create(unit=unit, service_charge=service_charge, amount=amount_unit)
