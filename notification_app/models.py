from django.db import models

from building_app.models import Building,Unit

class Notification(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name='برای ساختمان')
    title = models.CharField(max_length=50, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    hits = models.ManyToManyField(Unit,verbose_name='بازدید')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'اعلان'
        verbose_name_plural = 'اعلانات'