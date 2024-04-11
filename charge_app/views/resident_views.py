from django.http import Http404
from django.utils import timezone
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from buildingManagement.mixins import AccessOwnerChargeStatusMixin, ResidentRequiredMixin
from charge_app.models import ServiceChargeStatus
from building_app.models import Building


class ChargeList(LoginRequiredMixin, ResidentRequiredMixin, ListView):
    model = ServiceChargeStatus
    template_name = 'resident/charge-list.html'

    def get_queryset(self):
        unit = self.request.user.unit
        qs = ServiceChargeStatus.objects.filter(unit=unit)
        return qs


class ChargeDetail(LoginRequiredMixin, ResidentRequiredMixin, AccessOwnerChargeStatusMixin, View):
    template_name = 'resident/charge-detail.html'

    def get(self, request, *args, **kwargs):
        context = {}
        service_charge_status = get_object_or_404(ServiceChargeStatus, pk=kwargs['pk'])

        n = str(request.user.unit.building.card_number)
        context['card_number'] = f'{n[0:4]}-{n[4:8]}-{n[8:12]}-{n[12:16]}'
        context['object'] = service_charge_status
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        receipt = request.FILES.get('receipt')
        service_charge_status = get_object_or_404(ServiceChargeStatus, pk=kwargs['pk'])

        service_charge_status.receipt = receipt
        service_charge_status.status = 'unpaid_waiting'
        service_charge_status.pay_time = timezone.now()
        service_charge_status.save()

        context['object'] = service_charge_status
        return render(request, self.template_name, context)


@login_required
def payment_charge(request, *args, **kwargs):  # send message function in zarinpal
    if request.user.is_manager:
        raise Http404('شما به این صفحه دسترسی ندارید!')
    unit = request.user.unit
    charge_status_pk = kwargs.get('charge_status_pk')
    service_charge_status = get_object_or_404(ServiceChargeStatus, id=charge_status_pk)
    amount = int(service_charge_status.amount)

    if service_charge_status.unit == unit and service_charge_status.is_paid() == False:
        # redirect to zarinpal - video 57 toplearn in local
        # CallBackUrl = f'{payment-charge-verify}/{charge_status_pk}'
        return redirect('/resident-panel/payment-charge-verify/' + str(charge_status_pk))

    raise Http404()


@login_required
def payment_charge_verify(request, *args, **kwargs):
    if request.user.is_manager:
        raise Http404('شما به این صفحه دسترسی ندارید!')
    # if result.status == 100:
    charge_status_pk = kwargs.get('charge_status_pk')
    service_charge_status = get_object_or_404(ServiceChargeStatus, id=charge_status_pk)
    amount = int(service_charge_status.amount)

    # change status payment in ServiceChargeStatus model
    service_charge_status.status = 'online_paid'
    service_charge_status.pay_time = timezone.now()
    service_charge_status.save()

    # change credit building
    building = request.user.unit.building
    building = get_object_or_404(Building, id=building.id)
    building.credit += amount
    building.save()

    context = {'status': 100}
    return render(request, 'resident/payment-verify.html', context)
