from django.urls import path

from .views import (
    login_page,
    login_page_otp,
    choice_user_type,
    manager_register_page,
    resident_register_page,
    logout_view,
)

app_name = 'account_app'


urlpatterns = [
    path('login/', login_page, name= "login_page"),
    path('login-otp/', login_page_otp, name= "login_page_otp"),
    path('choice-user-type/', choice_user_type, name= "choice_user_type"),
    path('manager-register/', manager_register_page, name= "manager_register_page"),
    path('resident-register/', resident_register_page, name= "resident_register_page"),
    path('logout/', logout_view, name= "logout"),
]
