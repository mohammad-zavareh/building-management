from django.db import models

class VipService(models.Model):
    MAX_UNIT_CHOICE = [
        ('10', 'کمتر از 10 واحد'),
        ('30', '11 تا 30 واحد'),
        ('50', '31 تا 50 واحد'),
        ('100', '51 تا 100 واحد'),
        ('300', '100 تا 300 واحد'),
        ('500', '300 تا 500 واحد'),
        ('5000', 'بیشتر از 500 واحد'),
    ]
    NAME_CHOICE = [
        ('پلن طلایی', 'پلن طلایی'),
        ('پلن نقره ای', 'پلن نقره ای'),
        ('پلن برنزی', 'پلن برنزی'),
    ]
    name = models.CharField(choices=NAME_CHOICE,max_length=50, verbose_name='نام')
    slug = models.SlugField(max_length=60, verbose_name='نامک')
    price = models.IntegerField(verbose_name='مبلغ')
    time = models.IntegerField(verbose_name='مدت زمان به ماه')
    max_unit = models.CharField(choices=MAX_UNIT_CHOICE, max_length=50, verbose_name='حداکثر واحد')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'سرویس ویژه'
        verbose_name_plural = 'سرویس های ویژه'
