from django.http import Http404
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from  buildingManagement.mixins import AccessOwnerChargeStatusMixin
from charge_app.models import ServiceChargeStatus
from building_app.models import Building


class ChargeList(LoginRequiredMixin, ListView):
    model = ServiceChargeStatus
    template_name = 'resident/charge-list.html'

    def get_queryset(self):
        unit = self.request.user.unit
        qs = ServiceChargeStatus.objects.filter(unit=unit)
        return qs



class ChargeDetail(LoginRequiredMixin,AccessOwnerChargeStatusMixin, DetailView):
    model = ServiceChargeStatus
    template_name = 'resident/charge-detail.html'



@login_required
def payment_charge(request, *args, **kwargs):  # send message function in zarinpal
    unit = request.user.unit
    charge_status_pk = kwargs.get('charge_status_pk')
    service_charge_status = get_object_or_404(ServiceChargeStatus, id=charge_status_pk)
    amount = int(service_charge_status.amount)

    if service_charge_status.unit == unit and service_charge_status.is_paid == False:
        # redirect to zarinpal - video 57 toplearn in local
        # CallBackUrl = f'{payment-charge-verify}/{charge_status_pk}'
        return redirect('/resident-panel/payment-charge-verify/' + str(charge_status_pk))

    raise Http404()


@login_required
def payment_charge_verify(request, *args, **kwargs):
    # if result.status == 100:
    charge_status_pk = kwargs.get('charge_status_pk')
    service_charge_status = get_object_or_404(ServiceChargeStatus, id=charge_status_pk)
    amount = int(service_charge_status.amount)

    # change status payment in ServiceChargeStatus model
    service_charge_status.is_paid = True
    service_charge_status.pay_time = timezone.now()
    service_charge_status.save()

    # change credit building
    building = request.user.unit.building
    building = get_object_or_404(Building, id=building.id)
    building.credit += amount
    building.save()

    context = {'status': 100}
    return render(request, 'resident/payment-verify.html', context)
