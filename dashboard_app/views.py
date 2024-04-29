from django.views.generic import TemplateView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from buildingManagement.mixins import ManagerRequiredMixin, ResidentRequiredMixin
from charge_app.models import ServiceCharge, ServiceChargeStatus
from notification_app.models import Notification
from poll_app.models import Poll
from payment_request_app.models import RequestPayment


class ManagerDashboard(LoginRequiredMixin, ManagerRequiredMixin, TemplateView):
    template_name = 'manager_dashboard.html'

    def get_context_data(self, **kwargs):
        building = self.request.user.unit.building
        context = super().get_context_data(**kwargs)

        last_poll = Poll.objects.filter(building=building).last()
        context['question_poll'] = last_poll.question
        context['poll_options'] = last_poll.get_option()

        payment_requests = RequestPayment.objects.filter(building=building).order_by('-request_time')
        if len(payment_requests) > 5:
            request_length = len(payment_requests)
            payment_requests = payment_requests[request_length - 5:]
        context['last_five_request'] = payment_requests

        service_charge = ServiceCharge.objects.filter(building=building).order_by('-created')
        if len(service_charge) > 5:
            service_charge = service_charge[len(service_charge) - 5:]
        context['last_five_service_charge'] = service_charge

        notifications = Notification.objects.filter(building=building).order_by('-created')
        if len(notifications) > 5:
            notifications = notifications[len(notifications) - 5:]
        context['notifications'] = notifications

        context['building'] = building

        return context


class ResidentDashboard(LoginRequiredMixin, ResidentRequiredMixin, TemplateView):
    template_name = 'resident_dashboard.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        unit = self.request.user.unit
        building = self.request.user.unit.building

        not_participated_polls = Poll.objects.filter(Q(building=building), ~Q(polloption__units=unit))

        data['unpaid_charges'] = ServiceChargeStatus.objects.filter(Q(unit=unit), Q(status='unpaid_reject') |
                                                                    Q(status='unpaid_waiting') | Q(status='unpaid'))[
                                 0:3]
        data['not_participated_polls'] = not_participated_polls
        data['unseen_notifications'] = Notification.objects.filter(Q(building_id=building),
                                                                   ~Q(hits=unit)).order_by('-created')[0:3]
        return data
