from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from building_app.mixins import (
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
    VipService
)


class ManagerPanel(LoginRequiredMixin, ManagerRequiredMixin, TemplateView):
    template_name = 'manager/home.html'


# -----------------------------------------------------------------------------unit

class UnitList(LoginRequiredMixin, ManagerRequiredMixin, ListView):
    template_name = 'manager/unit-list.html'
    model = Unit
    paginate_by = 10

    def get_queryset(self):
        building = self.request.user.unit.building
        queryset = Unit.objects.filter(building=building).order_by('-is_manager')
        return queryset


class UpdateUnit(LoginRequiredMixin, ManagerRequiredMixin, ManagerAccessOwnerUnitMixin, UpdateView):
    model = Unit
    fields = ['name', 'number_of_member']
    template_name = 'manager/update-unit.html'
    success_url = reverse_lazy('building_app_manager:unit_list')

    # def get_queryset(self):
    #     if self.kwargs['pk'] == '2':
    #         return super().get_queryset()
    #     else:
    #         raise Http404('شما به این صفحه دسترسی ندارید')


# -----------------------------------------------------------------------------charge

class ChargeList(LoginRequiredMixin, ManagerRequiredMixin, ListView):
    template_name = 'manager/charge-list.html'
    paginate_by = 10

    def get_queryset(self):
        building = self.request.user.unit.building
        queryset = ServiceCharge.objects.filter(building=building)
        return queryset


class CreateCharge(LoginRequiredMixin, ManagerRequiredMixin, CreateView):
    model = ServiceCharge
    template_name = 'manager/create-charge.html'
    fields = ["title", "description", 'amount', 'divide_amount', "category", "expire_time"]
    success_url = reverse_lazy('building_app_manager:charge_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.building = self.request.user.unit.building
        self.object.save()
        return super().form_valid(form)


class UpdateCharge(LoginRequiredMixin, ManagerRequiredMixin, ManagerAccessOwnerChargeMixin, UpdateView):
    model = ServiceCharge
    template_name = 'manager/update-charge.html'
    fields = ["title", "description", "category", "expire_time"]
    success_url = reverse_lazy('building_app_manager:charge_list')


class ChargeStatus(LoginRequiredMixin, ManagerRequiredMixin, ManagerAccessOwnerChargeMixin, DetailView):
    model = ServiceCharge
    template_name = 'manager/charge-status.html'

    def get_context_data(self, *args, **kwargs):
        pk = self.kwargs['pk']
        context = super(ChargeStatus, self).get_context_data(*args, **kwargs)
        context['status_list'] = ServiceChargeStatus.objects.filter(service_charge_id=pk)
        context['charge_name'] = ServiceCharge.objects.get(id=pk)
        return context


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


# -----------------------------------------------------------------------------management

class VipServiceList(LoginRequiredMixin, ManagerRequiredMixin, ListView):
    model = VipService
    template_name = 'manager/vip-service-list.html'


class VipServiceDetail(LoginRequiredMixin, ManagerRequiredMixin, DetailView):
    model = VipService
    template_name = 'manager/vip-service-detail.html'
