from django.urls import path

from building_app.views.managerView import (
    ManagerPanel,
)

app_name = 'building_app_manager'

urlpatterns = [
    path('/', ManagerPanel.as_view(), name='home'),
]
