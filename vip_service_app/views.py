from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView,DetailView
from buildingManagement.mixins import ManagerRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from datetime import datetime
from dateutil.relativedelta import relativedelta

from .models import VipService

class VipServiceList(LoginRequiredMixin, ManagerRequiredMixin, ListView):
    model = VipService
    template_name = 'vip-service-list.html'

    def get_queryset(self):
        max_unit_of_building = self.request.user.building.max_unit
        vip_service = self.model.objects.filter(max_unit=max_unit_of_building)
        return vip_service


class VipServiceDetail(LoginRequiredMixin, ManagerRequiredMixin, DetailView):
    model = VipService
    template_name = 'vip-service-detail.html'



@login_required
def payment_vip_service(request, *args, **kwargs):
    building = request.user.building
    slug = kwargs.get('slug')
    vip_service = get_object_or_404(VipService, slug=slug)
    amount = int(vip_service.price)

    if building.is_vip():
        raise Http404('شما در حال حاضر پلن VIP دارید!')
    elif vip_service.max_unit != building.max_unit:
        raise Http404('امکان خرید این پلن برای شما وجود ندارد!')
    else:
        # redirect to zarinpal - video 57 toplearn in local
        # CallBackUrl = f'{payment-charge-verify}/{charge_status_pk}'
        return redirect('/manager-panel/payment-vip-service-verify/' + str(slug))

@login_required
def payment_vip_service_verify(request, *args, **kwargs):
    # if result.status == 100:
    building = request.user.building
    slug = kwargs.get('slug')
    vip_service = get_object_or_404(VipService, slug=slug)

    building.vip_plan = vip_service
    building.vip_time = datetime.now() + relativedelta(months=+vip_service.time)
    building.save()

    context = {'status': 100}
    return render(request, 'payment-vip-verify.html', context)
