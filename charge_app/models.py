from django.db import models
from django.db.models import Q

from django.db.models.signals import post_save

from django.dispatch import receiver
from django.utils import timezone

from account_app.models import User
from vip_service_app.models import VipService
from building_app.models import Building, Unit


class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name='عنوان')
    image = models.ImageField(upload_to='category', verbose_name='تصویر')
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ServiceCharge(models.Model):
    divide_type = [  # divide_members   divide_units
        ('member', 'تقسیم بر تعداد ساکنین'),
        ('unit', 'تقسیم بر تعداد واحد ها')
    ]

    building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name='برای ساختمان')
    title = models.CharField(max_length=30, verbose_name='عنوان')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')
    amount = models.IntegerField(default=0, verbose_name='مبلغ')
    divide_amount = models.CharField(max_length=30, choices=divide_type, verbose_name='تقسیم مبلغ')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
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

    def get_sum_unpaid_status_charge(self):
        qs = self.servicechargestatus_set.all().filter(Q(status='unpaid') | Q(status='unpaid_waiting') |
                                                       Q(status='unpaid_reject'))
        return len(qs)

    def get_sum_paid_status_charge(self):
        qs = self.servicechargestatus_set.all().filter(Q(status='online_paid') | Q(status='offline_paid'))
        return len(qs)


class ServiceChargeStatus(models.Model):
    STATUS_CHOICE = (
        ('online_paid', 'پرداخت شده - آنلاین'),
        ('offline_paid', 'پرداخت شده - آفلاین'),
        ('unpaid', 'پرداخت نشده'),
        ('unpaid_waiting', 'پرداخت نشده - در انتظار بررسی'),
        ('unpaid_reject', 'پرداخت نشده - رد شده'),
    )
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name='واحد')
    service_charge = models.ForeignKey(ServiceCharge, on_delete=models.CASCADE, verbose_name='شارژ خدمات')
    amount = models.IntegerField(verbose_name='مبلغ قابل پرداخت واحد')
    status = models.CharField(choices=STATUS_CHOICE, verbose_name='وضعیت پرداخت', max_length=50, default='unpaid')
    receipt = models.ImageField(upload_to='receipt', blank=True, null=True, verbose_name='رسید کارت به کارت')
    pay_time = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')

    def __str__(self):
        return f'{self.service_charge} => {self.unit}'

    class Meta:
        verbose_name = 'وضعیت شارژ خدمات'
        verbose_name_plural = 'وضعیت شارژهای خدمات'

    def status_is_waiting(self):
        if self.status == 'unpaid_waiting':
            return True
        else:
            return False

    def status_is_reject(self):
        if self.status == 'unpaid_reject':
            return True
        else:
            return False

    def is_paid(self):
        if self.status in ['online_paid', 'offline_paid']:
            return True
        else:
            return False

    def unpaid(self):
        if self.status in ['unpaid', 'unpaid_waiting', 'unpaid_reject']:
            return True
        else:
            return False

    def get_verbose_status(self):
        return dict(self.STATUS_CHOICE)[self.status]


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
