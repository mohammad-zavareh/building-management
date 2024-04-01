from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django import forms

from buildingManagement.mixins import (
    ManagerRequiredMixin,
    AccessOwnerChargeMixin,
)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from charge_app.models import ServiceCharge, ServiceChargeStatus


class ChargeList(LoginRequiredMixin, ManagerRequiredMixin, ListView):
    template_name = 'manager/charge-list.html'
    paginate_by = 10

    def get_queryset(self):
        building = self.request.user.building
        queryset = ServiceCharge.objects.filter(building=building)
        return queryset


class CreateCharge(LoginRequiredMixin, ManagerRequiredMixin, CreateView):
    model = ServiceCharge
    template_name = 'manager/create-charge.html'
    fields = ["title", "description", 'amount', 'divide_amount', "category", "expire_time"]
    success_url = reverse_lazy('charge_app_manager:charge_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['expire_time'].widget = forms.DateTimeInput(attrs={"type": "date"})
        return form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.building = self.request.user.building
        self.object.save()
        return super().form_valid(form)


class UpdateCharge(LoginRequiredMixin, ManagerRequiredMixin, AccessOwnerChargeMixin, UpdateView):
    model = ServiceCharge
    template_name = 'manager/update-charge.html'
    fields = ["title", "description", "category", "expire_time"]
    success_url = reverse_lazy('charge_app_manager:charge_list')


class ChargeStatus(LoginRequiredMixin, ManagerRequiredMixin, AccessOwnerChargeMixin, DetailView):
    model = ServiceCharge
    template_name = 'manager/charge-status.html'

    def get_context_data(self, *args, **kwargs):
        pk = self.kwargs['pk']
        context = super(ChargeStatus, self).get_context_data(*args, **kwargs)
        context['status_list'] = ServiceChargeStatus.objects.filter(service_charge_id=pk)
        context['charge_name'] = ServiceCharge.objects.get(id=pk)
        return context
