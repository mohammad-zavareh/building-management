from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from buildingManagement.mixins import ResidentRequiredMixin

from poll_app.models import Poll


class PollList(LoginRequiredMixin, ResidentRequiredMixin, ListView):
    model = Poll
    template_name = 'poll_list_resident.html'

    def get_queryset(self):
        building = self.request.user.unit.building
        return self.model.objects.filter(building=building)