from django.urls import path

from ..views.resident_views import NotificationList

app_name = 'notification_app_resident'

urlpatterns = [
    path('/notification-list', NotificationList.as_view(), name='notification_list'),
]
