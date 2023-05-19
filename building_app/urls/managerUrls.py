from django.urls import path

from building_app.views.managerView import (
    ManagerPanel,
    PaymentRequestList,
    CreatePaymentRequest,
    AddManager,
    ResignManager,
)

app_name = 'building_app_manager'

urlpatterns = [
    path('/', ManagerPanel.as_view(), name='home'),


    path('/add-manager', AddManager.as_view(), name='add_manager'),
    path('/resign-manager', ResignManager.as_view(), name='resign_manager'),
]
