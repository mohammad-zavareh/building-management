from django.http import Http404
from django.views.generic import ListView, CreateView, UpdateView, DetailView, View
from django import forms
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

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


class CheckPaymentRequest(LoginRequiredMixin, ManagerRequiredMixin, View):
    template_name = 'manager/check_payment-request.html'

    def get(self, request, *args, **kwargs):
        context = {}
        building = request.user.unit.building
        object_list = ServiceChargeStatus.objects.filter(Q(unit__building=building),
                                                         Q(status='unpaid_waiting') | Q(status='unpaid_reject'))
        context['object_list'] = object_list
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        object_pk = request.POST.get('object_pk')
        reject = request.POST.get('reject')
        accept = request.POST.get('accept')
        service_charge_status = get_object_or_404(ServiceChargeStatus, pk=object_pk)

        if service_charge_status.unit.building.manager != request.user:  # Only the owner can change the status
            raise Http404('شما به این صفحه دسترسی ندارید')

        if accept:
            service_charge_status.status = 'offline_paid'
            service_charge_status.save()
        elif reject:
            service_charge_status.status = 'unpaid_reject'
            service_charge_status.save()
        else:
            raise Http404()

        building = request.user.unit.building
        object_list = ServiceChargeStatus.objects.filter(Q(unit__building=building),
                                                         Q(status='unpaid_waiting') | Q(status='unpaid_reject'))
        context['object_list'] = object_list
        return render(request, self.template_name, context)

