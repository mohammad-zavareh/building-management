from django.urls import path
from poll_app.views.resident_views import PollList, Vote

app_name = 'poll_resident'

urlpatterns = [
    path('/poll-list', PollList.as_view(), name='poll_list'),
    path('/vote/<int:pk>', Vote.as_view(), name='vote'),
]