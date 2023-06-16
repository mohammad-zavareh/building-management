from django.urls import path

from account_app.views.login_views import login_account,verify_password,verify_otp,logout_view

app_name = 'account_app_login'

urlpatterns = [
    path('/login', login_account, name= 'login_account'),
    path('/login/verify-password', verify_password, name= 'verify_password'),
    path('/login/verify-otp', verify_otp, name= 'verify_otp'),
    path('/logout', logout_view, name= 'logout'),
]