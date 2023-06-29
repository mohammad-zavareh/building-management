from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Poll


class PollList(LoginRequiredMixin, ListView):
    model = Poll
    template_name_manager = 'poll_list_manager.html'
    template_name_resident = 'poll_list_resident.html'

    def get_queryset(self):
        if self.request.user.is_manager:
            building = self.request.user.building
        else:
            building = self.request.user.unit.building

        query_set = self.model.objects.filter(building=building)
        return query_set

    def get_template_names(self):
        if self.request.user.is_manager:
            return self.template_name_manager
        else:
            return self.template_name_resident