from django.urls import path

from .views import VipServiceList, VipServiceDetail

app_name = 'vip_service_app'

urlpatterns = [
    path('/pricing', VipServiceList.as_view(), name='vip_service_list'),
    path('/pricing/<slug>', VipServiceDetail.as_view(), name='vip_service_detail'),
]