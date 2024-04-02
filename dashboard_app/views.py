from django.views.generic import TemplateView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from buildingManagement.mixins import ManagerRequiredMixin, ResidentRequiredMixin
from charge_app.models import ServiceChargeStatus
from notification_app.models import Notification
from poll_app.models import Poll


class ManagerDashboard(LoginRequiredMixin, ManagerRequiredMixin, TemplateView):
    template_name = 'manager_dashboard.html'


class ResidentDashboard(LoginRequiredMixin, ResidentRequiredMixin, TemplateView):
    template_name = 'resident_dashboard.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        unit = self.request.user.unit
        building = self.request.user.unit.building

        not_participated_polls = Poll.objects.filter(Q(building=building), ~Q(polloption__units=unit))

        data['unpaid_charges'] = ServiceChargeStatus.objects.filter(unit=unit, is_paid=False)[0:3]
        data['not_participated_polls'] = not_participated_polls
        data['unseen_notifications'] = Notification.objects.filter(Q(building_id=building),
                                                                   ~Q(hits=unit)).order_by('-created')[0:3]
        return data
