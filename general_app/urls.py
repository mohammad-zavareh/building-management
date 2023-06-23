from django.urls import path

from .views import home, about_us, contact_us

app_name= 'general_app'

urlpatterns = [
    path('', home, name='home'),
    path('about-us', about_us, name='about-us'),
    path('contact-us', contact_us, name='contact-us'),
]
