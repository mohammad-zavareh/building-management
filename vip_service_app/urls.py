from django.urls import path

from .views import (
    VipServiceList,
    VipServiceDetail,
    payment_vip_service,
    payment_vip_service_verify
)

app_name = 'vip_service_app'

urlpatterns = [
    path('/pricing', VipServiceList.as_view(), name='vip_service_list'),
    path('/pricing/<slug>', VipServiceDetail.as_view(), name='vip_service_detail'),
    path('/payment-vip-service/<slug:slug>', payment_vip_service, name='payment_vip_service'),
    path('/payment-vip-service-verify/<slug:slug>', payment_vip_service_verify, name='payment_vip_service_verify'),
]