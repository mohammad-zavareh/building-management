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


# -----------------------------------------------------------------------------management


class AddManager(LoginRequiredMixin, ManagerRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        pk = request.GET.get('pk')

        unit = Unit.objects.filter(id=pk).first()
        unit.is_manager = True
        unit.save()
        message = {
            'text': 'کاربر مورد نظر با موفقیت با مدیر ساختمان شد',
            'tag': 'success'
        }
        return render(request, 'manager/partial/alert-message.html', message)


class ResignManager(LoginRequiredMixin, ManagerRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(request, 'manager/resign-manager.html', {})

    def post(self, request, *args, **kwargs):
        unit = request.user.unit
        building = request.user.unit.building
        number_of_manager = Unit.objects.filter(building=building, is_manager=True).count()
        message = {
            'text': '',
            'teg': '',
        }

        if number_of_manager > 1:
            unit.is_manager = False
            unit.save()

            message['text'] = 'استعفای شما با وفقیت انجام شد. از این پس شما فقط به پنل ساکنین دسترسی دارید'
            message['tag'] = 'success'
        else:
            message['text'] = 'تنها مدیر این ساختمان شما هستید. ابتدا فرد دیگری را مدیر ساختمان کنید'
            message['tag'] = 'warning'

        return render(request, 'manager/partial/alert-message.html', message)
