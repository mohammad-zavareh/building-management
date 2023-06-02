from django.urls import path

from charge_app.views.resident_views import ChargeList

app_name = 'charge_app_resident'

urlpatterns = [
    path('/charge-list', ChargeList.as_view(), name='charge_list'),
]
