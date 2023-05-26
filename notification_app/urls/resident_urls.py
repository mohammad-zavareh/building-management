from django.urls import path

from ..views.resident_views import NotificationList,NotificationFilter

app_name = 'notification_app_resident'

urlpatterns = [
    path('/notification-list', NotificationList.as_view(), name='notification_list'),
    path('/notification-list/filter/<str:filter>', NotificationFilter.as_view(), name='notification_filter'),
]