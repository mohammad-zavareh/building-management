from django.urls import path

from ..views.resident_views import NotificationList, NotificationDetail, NotificationFilter

app_name = 'notification_app_resident'

urlpatterns = [
    path('/notification-list', NotificationList.as_view(), name='notification_list'),
    path('/notification-detail/<int:pk>', NotificationDetail.as_view(), name='notification_detail'),
    path('/notification-list/filter/<str:filter>', NotificationFilter.as_view(), name='notification_filter'),
]
