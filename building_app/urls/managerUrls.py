from django.urls import path

from building_app.views.managerView import (
    ManagerPanel,
    NotificationList,
    CreateNotification,
    UpdateNotification,
    PaymentRequestList,
    CreatePaymentRequest,
    AddManager,
    ResignManager,
)

app_name = 'building_app_manager'

urlpatterns = [
    path('/', ManagerPanel.as_view(), name='home'),

    path('/payment-request-list', PaymentRequestList.as_view(), name='payment_request_list'),
    path('/create-payment-request', CreatePaymentRequest.as_view(), name='create_payment_request'),
    path('/add-manager', AddManager.as_view(), name='add_manager'),
    path('/resign-manager', ResignManager.as_view(), name='resign_manager'),
]
