from django.urls import path
from poll_app.views import PollList

app_name = 'poll_resident'

urlpatterns = [
    path('/poll-list', PollList.as_view(), name='poll_list')
]