from django.urls import path

from .views import ManagerDashboard,ResidentDashboard

app_name = 'dashboard_app'

urlpatterns = [
    path('/dashboard', ManagerDashboard.as_view(), name='manager_dashboard'),
    path('/dashboard', ResidentDashboard.as_view(), name='resident_dashboard'),
]