from django.urls import path

from .views import AddManager, ResignManager

app_name = 'management_manager_app'

urlpatterns = [
    path('/add-manager', AddManager.as_view(), name='add_manager'),
    path('/resign-manager', ResignManager.as_view(), name='resign_manager'),
]