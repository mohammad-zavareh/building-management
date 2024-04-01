from django.urls import path
from poll_app.views.manager_views import PollList, CreatePoll, ResultPoll, DetailVote, UpdatePoll

app_name = 'poll_manager'

urlpatterns = [
    path('/poll-list', PollList.as_view(), name='poll_list'),
    path('/create-poll', CreatePoll.as_view(), name='create_poll'),
    path('/update-poll/<pk>', UpdatePoll.as_view(), name='update_poll'),
    path('/result-poll/<pk>', ResultPoll.as_view(), name='result_poll'),
    path('/detail-vote/<pk>', DetailVote.as_view(), name='detail_vote'),
]