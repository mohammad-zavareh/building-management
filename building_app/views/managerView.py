from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from buildingManagement.mixins import (
    ManagerRequiredMixin,
    ManagerAccessOwnerNotificationMixin,
)

from building_app.models import (
    Unit,
)


class ManagerPanel(LoginRequiredMixin, ManagerRequiredMixin, TemplateView):
    template_name = 'manager/home.html'

