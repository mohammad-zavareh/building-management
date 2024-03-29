"""buildingManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('dashboard_app.urls')),
    path('', include('general_app.urls')),
    path('account', include('account_app.urls.register_urls')),
    path('account', include('account_app.urls.login_urls')),

    path('manager-panel', include('building_app.urls')),
    path('manager-panel', include('vip_service_app.urls')),
    path('manager-panel', include('charge_app.urls.manager_urls')),
    path('manager-panel', include('notification_app.urls.manager_urls')),
    path('manager-panel', include('payment_request_app.urls')),
    path('manager-panel', include('poll_app.urls.manager_urls')),

    path('resident-panel', include('notification_app.urls.resident_urls')),
    path('resident-panel', include('charge_app.urls.resident_urls')),
    path('resident-panel', include('poll_app.urls.resident_urls')),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
