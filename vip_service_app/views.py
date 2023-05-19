from django.views.generic import ListView,DetailView

from buildingManagement.mixins import ManagerRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import VipService

class VipServiceList(LoginRequiredMixin, ManagerRequiredMixin, ListView):
    model = VipService
    template_name = 'vip-service-list.html'


class VipServiceDetail(LoginRequiredMixin, ManagerRequiredMixin, DetailView):
    model = VipService
    template_name = 'vip-service-detail.html'