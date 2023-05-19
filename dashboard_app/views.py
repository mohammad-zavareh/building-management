from django.views.generic import TemplateView

from buildingManagement.mixins import ManagerRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class ManagerDashboard(LoginRequiredMixin, ManagerRequiredMixin,TemplateView):
    template_name = 'manager_dashboard.html'

class ResidentDashboard(LoginRequiredMixin,TemplateView):
    template_name = 'resident_dashboard.html'
