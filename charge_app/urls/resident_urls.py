from django.urls import path

from charge_app.views.resident_views import ChargeList,ChargeDetail, payment_charge,payment_charge_verify

app_name = 'charge_app_resident'

urlpatterns = [
    path('/charge-list', ChargeList.as_view(), name='charge_list'),
    path('/charge-detail/<int:pk>', ChargeDetail.as_view(), name='charge_detail'),
    path('/payment-charge/<int:charge_status_pk>', payment_charge, name='payment_charge'),
    path('/payment-charge-verify/<int:charge_status_pk>', payment_charge_verify, name='payment_charge_verify'),
]
