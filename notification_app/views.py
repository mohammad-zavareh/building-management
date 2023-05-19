from django.views.generic import ListView,UpdateView,CreateView


from buildingManagement.mixins import (
    ManagerRequiredMixin,
    ManagerAccessOwnerNotificationMixin
)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Notification

class NotificationList(LoginRequiredMixin, ManagerRequiredMixin, ListView):
    model = Notification
    template_name = 'manager/notification-list.html'
    paginate_by = 10

    def get_queryset(self):
        building = self.request.user.unit.building
        qs = super().get_queryset().filter(building=building)
        return qs


class CreateNotification(LoginRequiredMixin, ManagerRequiredMixin, CreateView):
    model = Notification
    template_name = 'manager/create-notification.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('notification_app:notification_list')

    def form_valid(self, form):
        building = self.request.user.unit.building

        self.object = form.save(commit=False)
        self.object.building = building
        self.object.save()

        return super().form_valid(form)


class UpdateNotification(LoginRequiredMixin, ManagerRequiredMixin, ManagerAccessOwnerNotificationMixin, UpdateView):
    model = Notification
    template_name = 'manager/update-notification.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('notification_app:notification_list')

