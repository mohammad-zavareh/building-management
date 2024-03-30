from django.views.generic import ListView, FormView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from buildingManagement.mixins import ManagerRequiredMixin
from django.urls import reverse_lazy

from poll_app.models import Poll, PollOption
from poll_app.forms import CreatePollForm


class PollList(LoginRequiredMixin, ManagerRequiredMixin, ListView):
    model = Poll
    template_name = 'poll_list_manager.html'
    paginate_by = 10

    def get_queryset(self):
        building = self.request.user.building
        return self.model.objects.filter(building=building)


class CreatePoll(LoginRequiredMixin, ManagerRequiredMixin, FormView):
    template_name = 'create_poll.html'
    form_class = CreatePollForm
    success_url = reverse_lazy('poll_manager:poll_list')

    def form_valid(self, form):
        building = self.request.user.building

        poll = Poll.objects.create(building=building, question=form.cleaned_data.get('question'))
        poll.save()

        for i in range(1, 7):
            option = form.cleaned_data.get(f'option_{i}')
            if option:
                PollOption.objects.create(poll=poll, option=option).save()
            else:
                break
        return super(CreatePoll, self).form_valid(form)


class ResultPoll(LoginRequiredMixin, ManagerRequiredMixin, DetailView):
    model = Poll
    template_name = 'result_poll.html'


class DetailVote(LoginRequiredMixin, ManagerRequiredMixin, DetailView):
    model = Poll
    template_name = 'result_vote.html'
