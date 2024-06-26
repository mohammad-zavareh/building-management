from django.http import HttpResponse
from django.views.generic import ListView, DetailView, FormView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from buildingManagement.mixins import AccessOwnerNotificationMixin, SaveVisitMixin, ResidentRequiredMixin
from notification_app.models import Notification, Comment


class NotificationList(LoginRequiredMixin, ResidentRequiredMixin, ListView):
    model = Notification
    template_name = 'resident/notification-list.html'
    paginate_by = 10

    def get_queryset(self):
        building = self.request.user.unit.building
        qs = super().get_queryset().filter(building=building).order_by('-created')
        return qs


class NotificationDetail(LoginRequiredMixin, ResidentRequiredMixin, AccessOwnerNotificationMixin, SaveVisitMixin,
                         DetailView):
    model = Notification
    template_name = 'resident/notification-detail.html'

    def get_context_data(self, **kwargs):
        context = super(NotificationDetail, self).get_context_data()
        context['comments'] = self.object.comment_set.all().order_by('-created')
        return context


class NotificationFilter(LoginRequiredMixin, ResidentRequiredMixin, ListView):
    model = Notification
    template_name = 'resident/notification-list.html'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        building = self.request.user.unit.building
        unit = self.request.user.unit

        filter = self.kwargs['filter']

        if filter == 'seen':
            qs = Notification.objects.filter(Q(building_id=building), Q(hits=unit)).order_by(
                '-created')  # notification seen by unit
        elif filter == 'unseen':
            qs = Notification.objects.filter(Q(building_id=building), ~Q(hits=unit)).order_by(
                '-created')  # notification unseen by unit
        else:
            qs = Notification.objects.filter(building_id=building).order_by('-created')  # all notification

        return qs


def notification_comment(request):
    if request.POST:
        comment = request.POST.get('comment')
        notifi_id = request.POST.get('notifi_id')
        unit = request.user.unit
        Comment.objects.create(notification_id=notifi_id, unit=unit, text=comment).save()
    return HttpResponse()
