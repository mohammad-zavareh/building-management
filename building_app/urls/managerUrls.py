from django.urls import path

from building_app.views.managerView import (
    ManagerPanel,
    ChargeList,
    CreateCharge,
    UpdateCharge,
    ChargeStatus,
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

    path('/charge-list', ChargeList.as_view(), name='charge_list'),
    path('/create-charge', CreateCharge.as_view(), name='create_charge'),
    path('/charge-status/<pk>', ChargeStatus.as_view(), name='charge_status'),
    path('/update-charge/<pk>', UpdateCharge.as_view(), name='update_charge'),
    path('/notification-list', NotificationList.as_view(), name='notification_list'),
    path('/create-notification', CreateNotification.as_view(), name='create_notification'),
    path('/update-notification/<pk>', UpdateNotification.as_view(), name='update_notification'),
    path('/payment-request-list', PaymentRequestList.as_view(), name='payment_request_list'),
    path('/create-payment-request', CreatePaymentRequest.as_view(), name='create_payment_request'),
    path('/add-manager', AddManager.as_view(), name='add_manager'),
    path('/resign-manager', ResignManager.as_view(), name='resign_manager'),
]
