from django.db import models

class VipService(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام')
    slug = models.SlugField(max_length=10, verbose_name='نامک')
    price = models.IntegerField(verbose_name='مبلغ')
    time = models.IntegerField(verbose_name='مدت زمان به ماه')
    max_unit = models.IntegerField(verbose_name='حداکثر واحد')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'سرویس ویژه'
        verbose_name_plural = 'سرویس های ویژه'