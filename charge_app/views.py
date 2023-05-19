from django.views.generic import ListView, CreateView,UpdateView,DetailView

from buildingManagement.mixins import (
    ManagerRequiredMixin,
    ManagerAccessOwnerChargeMixin,
)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import ServiceCharge,ServiceChargeStatus

class ChargeList(LoginRequiredMixin, ManagerRequiredMixin, ListView):
    template_name = 'manager/charge-list.html'
    paginate_by = 10

    def get_queryset(self):
        building = self.request.user.unit.building
        queryset = ServiceCharge.objects.filter(building=building)
        return queryset


class CreateCharge(LoginRequiredMixin, ManagerRequiredMixin, CreateView):
    model = ServiceCharge
    template_name = 'manager/create-charge.html'
    fields = ["title", "description", 'amount', 'divide_amount', "category", "expire_time"]
    success_url = reverse_lazy('charge_app:charge_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.building = self.request.user.unit.building
        self.object.save()
        return super().form_valid(form)


class UpdateCharge(LoginRequiredMixin, ManagerRequiredMixin, ManagerAccessOwnerChargeMixin, UpdateView):
    model = ServiceCharge
    template_name = 'manager/update-charge.html'
    fields = ["title", "description", "category", "expire_time"]
    success_url = reverse_lazy('charge_app:charge_list')


class ChargeStatus(LoginRequiredMixin, ManagerRequiredMixin, ManagerAccessOwnerChargeMixin, DetailView):
    model = ServiceCharge
    template_name = 'manager/charge-status.html'

    def get_context_data(self, *args, **kwargs):
        pk = self.kwargs['pk']
        context = super(ChargeStatus, self).get_context_data(*args, **kwargs)
        context['status_list'] = ServiceChargeStatus.objects.filter(service_charge_id=pk)
        context['charge_name'] = ServiceCharge.objects.get(id=pk)
        return context
