from django.views.generic import View
from django.shortcuts import render

from account_app.models import User

from buildingManagement.mixins import ManagerRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class AddManager(LoginRequiredMixin, ManagerRequiredMixin, View):
    def get(self, request, *args, **kwargs):

        user = request.user
        user.is_manager = True
        user.save()
        message = {
            'text': 'کاربر مورد نظر با موفقیت با مدیر ساختمان شد',
            'tag': 'success'
        }
        return render(request, 'manager/partial/alert-message.html', message)


class ResignManager(LoginRequiredMixin, ManagerRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(request, 'manager/resign-manager.html', {})

    def post(self, request, *args, **kwargs):
        user = request.user
        building = request.user.unit.building
        number_of_manager = User.objects.filter(is_manager=True,building=building).count()
        message = {
            'text': '',
            'teg': '',
        }

        if number_of_manager > 1:
            user.is_manager = False
            user.save()

            message['text'] = 'استعفای شما با وفقیت انجام شد. از این پس شما فقط به پنل ساکنین دسترسی دارید'
            message['tag'] = 'success'
        else:
            message['text'] = 'تنها مدیر این ساختمان شما هستید. ابتدا فرد دیگری را مدیر ساختمان کنید'
            message['tag'] = 'warning'

        return render(request, 'manager/partial/alert-message.html', message)
