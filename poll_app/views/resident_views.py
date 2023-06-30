from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from buildingManagement.mixins import ResidentRequiredMixin

from poll_app.models import Poll, PollOption


class PollList(LoginRequiredMixin, ResidentRequiredMixin, ListView):
    model = Poll
    template_name = 'poll_list_resident.html'

    def get_queryset(self):
        building = self.request.user.unit.building
        return self.model.objects.filter(building=building)


class Vote(LoginRequiredMixin, ResidentRequiredMixin, DetailView):
    model = Poll
    template_name = 'vote.html'

    def get(self, request, **kwargs):
        if request.method == 'GET':
            self.object = super(Vote, self).get_object()
            context = super(DetailView, self).get_context_data(**kwargs)

            unit = request.user.unit
            if unit in self.object.get_votes():
                pre_selected = PollOption.objects.filter(poll=self.object, units=unit).first()
                context['pre_selected'] = pre_selected

            return self.render_to_response(context=context)

    def post(self, request, **kwargs):
        if request.method == 'POST':
            self.object = super(Vote, self).get_object()
            context = super(DetailView, self).get_context_data(**kwargs)

            selected_option = request.POST.get('option')
            if selected_option is None:
                raise Http404()
            option = PollOption.objects.filter(poll=self.object, option=selected_option).first()
            unit = request.user.unit

            if unit not in self.object.get_votes():
                option.units.add(unit)
                context['message'] = 'ثبت شد!'
            else:
                context['message'] = 'شما از قبل در این نظر سنجی شرکت کرده اید!'
            return self.render_to_response(context=context)
