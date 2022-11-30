from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from building_app.models import (
    Building,
    Unit,
    Category,
    ServiceCharge,
    ServiceChargeStatus,
    Notification
)

class ResidentPanel(LoginRequiredMixin, TemplateView):
    template_name = 'resident/home.html'
