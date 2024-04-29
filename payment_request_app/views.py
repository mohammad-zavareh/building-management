from django.views.generic import ListView,CreateView

from buildingManagement.mixins import ManagerRequiredMixin

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import RequestPayment


class PaymentRequestList(LoginRequiredMixin, ManagerRequiredMixin, ListView):
    model = RequestPayment
    template_name = 'manager/request-payment-list.html'
    paginate_by = 10

    def get_queryset(self):
        building = self.request.user.building
        queryset = super().get_queryset().filter(building=building)
        return queryset


class CreatePaymentRequest(LoginRequiredMixin, ManagerRequiredMixin, CreateView):
    model = RequestPayment
    template_name = 'manager/create-request-payment.html'
    fields = ['sheba_number', 'amount']
    success_url = reverse_lazy('payment_request_app:payment_request_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['credit'] = self.request.user.building.credit
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)

        credit = self.request.user.building.credit
        amount = self.object.amount
        if credit >= amount:
            building = self.request.user.building

            building.credit -= amount
            building.save()

            self.object.building = building
            self.object.save()
            return super().form_valid(form)
        else:
            form.add_error('amount', 'مبلغ وارد شده از موجودی شما بیشتر میباشد!')
            return super().form_invalid(form)
