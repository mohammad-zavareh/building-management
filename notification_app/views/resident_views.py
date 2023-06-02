from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from buildingManagement.mixins import AccessOwnerNotificationMixin,SaveVisitMixin
from notification_app.models import Notification


class NotificationList(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'resident/notification-list.html'
    paginate_by = 10

    def get_queryset(self):
        building = self.request.user.unit.building
        qs = super().get_queryset().filter(building=building).order_by('-created')
        return qs

class NotificationDetail(LoginRequiredMixin,AccessOwnerNotificationMixin,SaveVisitMixin, DetailView):
    model = Notification
    template_name = 'resident/notification-detail.html'



class NotificationFilter(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'resident/notification-list.html'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        building = self.request.user.unit.building
        unit = self.request.user.unit

        filter = self.kwargs['filter']

        if filter == 'seen':
            qs = Notification.objects.filter(Q(building_id=building),Q(hits=unit)).order_by('-created') # notification seen by unit
        elif filter == 'unseen':
            qs = Notification.objects.filter(Q(building_id=building),~Q(hits=unit)).order_by('-created') # notification unseen by unit
        else:
            qs = Notification.objects.filter(building_id=building).order_by('-created') # all notification

        return qs
