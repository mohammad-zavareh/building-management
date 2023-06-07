from django.contrib import admin
from django.utils.html import format_html

from .models import ServiceCharge,ServiceChargeStatus, Category


class ServiceChargeAdmin(admin.ModelAdmin):
    list_display = ('title','building','category', 'is_active')
    list_filter = ('expire_time',)
    ordering = ('title',)
    search_fields = ('title', 'description')


class ServiceChargeStatusAdmin(admin.ModelAdmin):
    list_display = ('unit', 'service_charge', 'is_paid')
    list_filter = ('unit', 'service_charge', 'is_paid')
    search_fields = ('unit.name', 'service_charge.title')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag',)
    list_filter = ('is_active',)
    ordering = ('title',)
    search_fields = ('title',)

    def image_tag(self, obj):
        return format_html(f'<img src="{obj.image.url}" with="25px" height="25px"/>')




admin.site.register(ServiceCharge, ServiceChargeAdmin)
admin.site.register(ServiceChargeStatus, ServiceChargeStatusAdmin)
admin.site.register(Category, CategoryAdmin)