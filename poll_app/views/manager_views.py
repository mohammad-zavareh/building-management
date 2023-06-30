from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from buildingManagement.mixins import ManagerRequiredMixin

from poll_app.models import Poll


class PollList(LoginRequiredMixin, ManagerRequiredMixin, ListView):
    model = Poll
    template_name = 'poll_list_manager.html'

    def get_queryset(self):
        building = self.request.user.building
        return self.model.objects.filter(building=building)