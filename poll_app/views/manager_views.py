from django.views.generic import ListView, FormView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from buildingManagement.mixins import ManagerRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect

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


class UpdatePoll(LoginRequiredMixin, ManagerRequiredMixin, View):
    template_name = 'update_poll.html'

    def get(self, request, *args, **kwargs):
        context = {}
        poll_pk = kwargs['pk']
        poll = get_object_or_404(Poll, pk=poll_pk)
        options = poll.get_option()
        context['poll'] = poll
        context['options'] = options
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        poll_pk = kwargs['pk']
        poll = get_object_or_404(Poll, pk=poll_pk)
        options = poll.get_option()

        form = request.POST

        poll.question = form.get('question')
        poll.save()

        counter = 1
        for option in options:
            option_input = form.get(f'option_{counter}')
            if option_input:
                option.option = form.get(f'option_{counter}')
                option.save()
                context['result_message'] = 'ویرایش شد!'
                counter += 1
            else:
                context['result_message'] = 'گزینه ها نمیتوانند خالی باشند'
                break

        context['poll'] = poll
        context['options'] = options
        return render(request, self.template_name, context)


class ResultPoll(LoginRequiredMixin, ManagerRequiredMixin, DetailView):
    model = Poll
    template_name = 'result_poll.html'


class DetailVote(LoginRequiredMixin, ManagerRequiredMixin, DetailView):
    model = Poll
    template_name = 'detail_vote.html'
