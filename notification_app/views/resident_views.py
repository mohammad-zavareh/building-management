from django.views.generic import ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

from notification_app.models import Notification

class NotificationList(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'resident/notification-list.html'
    paginate_by = 10

    def get_queryset(self):
        building = self.request.user.unit.building
        qs = super().get_queryset().filter(building=building).order_by('-created')
        return qs

