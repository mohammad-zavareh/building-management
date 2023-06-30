from django.urls import path
from poll_app.views.manager_views import PollList

app_name = 'poll_manager'

urlpatterns = [
    path('/poll-list', PollList.as_view(), name='poll_list')
]