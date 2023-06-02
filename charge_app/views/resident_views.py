from django.views.generic import ListView, CreateView,UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from charge_app.models import ServiceCharge,ServiceChargeStatus

class ChargeList(ListView):
    model = ServiceChargeStatus
    template_name = 'resident/charge-list.html'

    def get_queryset(self):
        unit = self.request.user.unit
        qs = ServiceChargeStatus.objects.filter(unit=unit)
        return qs