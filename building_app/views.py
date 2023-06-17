from django.views.generic import ListView,UpdateView

from .models import Unit

from buildingManagement.mixins import (
    ManagerRequiredMixin,
    ManagerAccessOwnerUnitMixin
)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class UnitList(LoginRequiredMixin, ManagerRequiredMixin, ListView):
    template_name = 'manager/unit-list.html'
    model = Unit
    paginate_by = 10

    def get_queryset(self):
        building = self.request.user.building
        queryset = Unit.objects.filter(building=building)
        return queryset


class UpdateUnit(LoginRequiredMixin, ManagerRequiredMixin, ManagerAccessOwnerUnitMixin, UpdateView):
    model = Unit
    fields = ['name', 'number_of_member']
    template_name = 'manager/update-unit.html'
    success_url = reverse_lazy('building_app:unit_list')