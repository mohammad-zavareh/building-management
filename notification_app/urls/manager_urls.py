from django.urls import path

from notification_app.views.manager_views import (
    NotificationList,
    CreateNotification,
    UpdateNotification,
)

app_name = 'notification_app_manager'

urlpatterns = [
    path('/notification-list', NotificationList.as_view(), name='notification_list'),
    path('/create-notification', CreateNotification.as_view(), name='create_notification'),
    path('/update-notification/<pk>', UpdateNotification.as_view(), name='update_notification'),
]
