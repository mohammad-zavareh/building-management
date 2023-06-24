from django.views.generic import ListView, UpdateView

from .models import Unit, Building

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


class UpdateBuilding(LoginRequiredMixin, ManagerRequiredMixin, UpdateView):
    model = Building
    fields = ['image', 'name', 'rules']
    template_name = 'manager/update-building.html'
    success_url = reverse_lazy('building_app:update_building')

    def get_object(self, queryset=None):
        building = Building.objects.filter(manager=self.request.user).first()
        return building


class UpdateUnit(LoginRequiredMixin, ManagerRequiredMixin, ManagerAccessOwnerUnitMixin, UpdateView):
    model = Unit
    fields = ['name', 'number_of_member']
    template_name = 'manager/update-unit.html'
    success_url = reverse_lazy('building_app:unit_list')
