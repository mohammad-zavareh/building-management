from django.urls import path

from .views import (ChargeList,
                    CreateCharge,
                    ChargeStatus,
                    UpdateCharge,
                    )

app_name = 'charge_app'

urlpatterns = [
    path('/charge-list', ChargeList.as_view(), name='charge_list'),
    path('/create-charge', CreateCharge.as_view(), name='create_charge'),
    path('/charge-status/<pk>', ChargeStatus.as_view(), name='charge_status'),
    path('/update-charge/<pk>', UpdateCharge.as_view(), name='update_charge'),
]
