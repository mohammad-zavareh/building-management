from django.urls import path
from account_app.views.register_views import (
    register_account,
    verify_otp,
    re_send_otp,
    register_building,
    register_unit,
)

app_name = 'account_app_register'

urlpatterns = [
    path('/register', register_account, name='register_account'),
    path('/register/verify-otp', verify_otp, name='verify_otp'),
    path('/register/re-send-otp/<int:phone_number>', re_send_otp, name='re_send_otp'),
    path('/register-building', register_building, name='register_building'),
    path('/register-unit', register_unit, name='register_unit'),
]
