from django.db import models
from django.utils import timezone

from building_app.models import Building, Unit


class Notification(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name='برای ساختمان')
    title = models.CharField(max_length=50, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    created = models.DateTimeField(default=timezone.now, verbose_name='زمان ایجاد')
    hits = models.ManyToManyField(Unit, verbose_name='بازدید', blank=True, null=True)

    def __str__(self):
        return self.title[0:20]

    class Meta:
        verbose_name = 'اعلان'
        verbose_name_plural = 'اعلانات'


class Comment(models.Model):
    notification = models.ForeignKey(Notification, verbose_name='اعلان', on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, verbose_name='واحد', on_delete=models.CASCADE)
    text = models.CharField(max_length=200, verbose_name='متن')
    created = models.DateTimeField(default=timezone.now, verbose_name='زمان ایجاد')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'
