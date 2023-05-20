from django.urls import path

from .views import ManagerDashboard,ResidentDashboard

app_name = 'dashboard_app'

urlpatterns = [
    path('manager-panel/dashboard', ManagerDashboard.as_view(), name='manager_dashboard'),
    path('resident-panel/dashboard', ResidentDashboard.as_view(), name='resident_dashboard'),
]