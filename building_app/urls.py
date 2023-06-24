from django.urls import path

from .views import UnitList,UpdateBuilding, UpdateUnit

app_name = 'building_app'

urlpatterns = [
    path('/unit-list', UnitList.as_view(), name='unit_list'),
    path('/update-building', UpdateBuilding.as_view(), name='update_building'),
    path('/update-unit/<pk>', UpdateUnit.as_view(), name='update_unit'),
]