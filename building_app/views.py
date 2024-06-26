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
    fields = ['image', 'name', 'max_unit', 'rules', 'card_number', 'card_type', 'owner_card']
    template_name = 'manager/update-building.html'
    success_url = reverse_lazy('building_app:update_building')

    def get_object(self, queryset=None):
        building = Building.objects.filter(manager=self.request.user).first()
        return building

    def form_valid(self, form):
        if self.request.user.building.is_vip():
            form.add_error('max_unit',
                           'شما در حال حاضر به دلیل عضو ویژه بودن قادر به ویرایش تعداد واحد های ساختمان نیستید!')
            return super().form_invalid(form)
        return super().form_valid(form)


class UpdateUnit(LoginRequiredMixin, ManagerRequiredMixin, ManagerAccessOwnerUnitMixin, UpdateView):
    model = Unit
    fields = ['name', 'number_of_member']
    template_name = 'manager/update-unit.html'
    success_url = reverse_lazy('building_app:unit_list')
