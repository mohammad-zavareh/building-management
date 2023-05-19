from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from buildingManagement.mixins import (
    ManagerRequiredMixin,
    ManagerAccessOwnerUnitMixin,
    ManagerAccessOwnerChargeMixin,
    ManagerAccessOwnerNotificationMixin,
)

from building_app.models import (
    RequestPayment,
    Unit,
    ServiceCharge,
    ServiceChargeStatus,
    Notification,
)


class ManagerPanel(LoginRequiredMixin, ManagerRequiredMixin, TemplateView):
    template_name = 'manager/home.html'


# -----------------------------------------------------------------------------notification
class NotificationList(LoginRequiredMixin, ManagerRequiredMixin, ListView):
    model = Notification
    template_name = 'manager/notification-list.html'
    paginate_by = 10

    def get_queryset(self):
        building = self.request.user.unit.building
        qs = super().get_queryset().filter(building=building)
        return qs


class CreateNotification(LoginRequiredMixin, ManagerRequiredMixin, CreateView):
    model = Notification
    template_name = 'manager/create-notification.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('building_app_manager:notification_list')

    def form_valid(self, form):
        building = self.request.user.unit.building

        self.object = form.save(commit=False)
        self.object.building = building
        self.object.save()

        return super().form_valid(form)


class UpdateNotification(LoginRequiredMixin, ManagerRequiredMixin, ManagerAccessOwnerNotificationMixin, UpdateView):
    model = Notification
    template_name = 'manager/update-notification.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('building_app_manager:notification_list')


# -----------------------------------------------------------------------------payment request


class PaymentRequestList(LoginRequiredMixin, ManagerRequiredMixin, ListView):
    model = RequestPayment
    template_name = 'manager/request-payment-list.html'
    paginate_by = 10

    def get_queryset(self):
        building = self.request.user.unit.building
        queryset = super().get_queryset().filter(building=building)
        return queryset


class CreatePaymentRequest(LoginRequiredMixin, ManagerRequiredMixin, CreateView):
    model = RequestPayment
    template_name = 'manager/create-request-payment.html'
    fields = ['sheba_number', 'amount']
    success_url = reverse_lazy('building_app_manager:payment_request_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['credit'] = self.request.user.unit.building.credit
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)

        credit = self.request.user.unit.building.credit
        amount = self.object.amount
        if credit >= amount:
            building = self.request.user.unit.building

            building.credit -= amount
            building.save()

            self.object.building = building
            self.object.save()
            return super().form_valid(form)
        else:
            form.add_error('amount', 'مبلغ وارد شده از موجودی شما بیشتر میباشد!')
            return super().form_invalid(form)


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
