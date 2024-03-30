from django.db import models
from building_app.models import Building, Unit


def weird_division(n, d):
    return n / d if d else 0


class Poll(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name='ساختمان')
    question = models.CharField(max_length=200, verbose_name='سوال')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')

    def __str__(self):
        return self.question[0:20]

    class Meta:
        verbose_name = ' سوال نظرسنجی'
        verbose_name_plural = ' سوالات نظرسنجی ها'

    def get_votes(self):
        votes = []
        options = self.polloption_set.all()

        for option in options:
            for unit in option.units.all():
                votes.append(unit.name)
        return votes

    def get_option(self):
        return self.polloption_set.all()


class PollOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name='سوال')
    units = models.ManyToManyField(Unit, related_name='votes', null=True, blank=True, verbose_name='رای دهندگان')
    option = models.CharField(max_length=50, verbose_name='گزینه')

    def __str__(self):
        return self.option[0:20]

    class Meta:
        verbose_name = 'گزینه نظرسنجی'
        verbose_name_plural = 'گزینه های نظرسنجی'

    def get_unit_that_vote(self):
        return self.units.all()

    def get_number_of_vote(self):
        units = self.units
        return len(units.all())

    def get_percent_option(self):
        total_votes = len(Poll.objects.get(polloption=self).get_votes())
        option_votes = self.get_number_of_vote()

        return round(weird_division(option_votes, total_votes) * 100)
