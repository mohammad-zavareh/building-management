from django.db import models
from building_app.models import Building, Unit


class Poll(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name='ساختمان')
    question = models.CharField(max_length=200, verbose_name='سوال')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')

    def __str__(self):
        return self.question[0:20]

    class Meta:
        verbose_name = ' سوال نظرسنجی'
        verbose_name_plural = ' سوالات نظرسنجی ها'


class PollOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name='سوال')
    units = models.ManyToManyField(Unit, related_name='votes', null=True, blank=True, verbose_name='رای دهندگان')
    option = models.CharField(max_length=50, verbose_name='گزینه')

    def __str__(self):
        return self.option[0:20]

    class Meta:
        verbose_name = 'گزینه نظرسنجی'
        verbose_name_plural = 'گزینه های نظرسنجی'
