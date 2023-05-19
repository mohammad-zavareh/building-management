from django.urls import path

from .views import PaymentRequestList, CreatePaymentRequest

app_name = 'payment_request_app'

urlpatterns = [
    path('/payment-request-list', PaymentRequestList.as_view(), name='payment_request_list'),
    path('/create-payment-request', CreatePaymentRequest.as_view(), name='create_payment_request'),
]
