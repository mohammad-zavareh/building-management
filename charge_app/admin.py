from django.contrib import admin

from .models import ServiceCharge,ServiceChargeStatus


class ServiceChargeAdmin(admin.ModelAdmin):
    list_display = ('title','building', 'get_categories', 'is_active')
    list_filter = ('expire_time',)
    ordering = ('title',)
    search_fields = ('title', 'description')


class ServiceChargeStatusAdmin(admin.ModelAdmin):
    list_display = ('unit', 'service_charge', 'is_paid')
    list_filter = ('unit', 'service_charge', 'is_paid')
    search_fields = ('unit.name', 'service_charge.title')

admin.site.register(ServiceCharge, ServiceChargeAdmin)
admin.site.register(ServiceChargeStatus, ServiceChargeStatusAdmin)