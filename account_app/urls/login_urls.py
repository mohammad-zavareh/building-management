from django.urls import path

from account_app.views.login_views import login_account, verify_password, verify_otp, set_otp, logout_view,re_send_otp

app_name = 'account_app_login'

urlpatterns = [
    path('/login', login_account, name='login_account'),
    path('/login/verify-password', verify_password, name='verify_password'),
    path('/login/set-otp', set_otp, name='set_otp'),
    path('/login/re-send-otp/<int:phone_number>', re_send_otp, name='re_send_otp'),
    path('/login/verify-otp', verify_otp, name='verify_otp'),
    path('/logout', logout_view, name='logout'),
]
