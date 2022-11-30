from django.urls import path

from building_app.views.residentView import ResidentPanel

app_name = 'building_app_resident'

urlpatterns = [
    path('/', ResidentPanel.as_view(), name='home'),
]
