from django.contrib import admin

from django.utils.html import format_html

from .models import (
    Building,
    RequestPayment,
    Notification,
    Unit,
    ServiceCharge,
    ServiceChargeStatus,
    Category,
    VipService,
)


class BuildingAdmin(admin.ModelAdmin):
    list_display = ('building_id', 'name', 'image_tag', 'is_vip')
    ordering = ('name',)
    search_fields = ('name',)

    def image_tag(self, obj):
        return format_html(f'<img src="{obj.image.url}" with="25px" height="25px"/>')

    image_tag.short_description = True


class RequestPaymentAdmin(admin.ModelAdmin):
    list_display = ('building', 'sheba_number',
                    'amount',
                    'paid',
                    'pay_time',
                    'request_time'
                    )

    list_filter = ('building','amount')
    ordering = ('request_time',)
    search_fields = ('sheba_number','building')


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'building')
    list_filter = ('building',)
    ordering = ('title',)
    search_fields = ('title',)


class VipServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'time', 'max_unit')
    prepopulated_fields = {'slug': ('name',)}


class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'building', 'is_manager')
    search_fields = ('name', 'building')


class ServiceChargeAdmin(admin.ModelAdmin):
    list_display = ('title','building', 'get_categories', 'is_active')
    list_filter = ('expire_time',)
    ordering = ('title',)
    search_fields = ('title', 'description')


class ServiceChargeStatusAdmin(admin.ModelAdmin):
    list_display = ('unit', 'service_charge', 'is_paid', 'payment_type_choice')
    list_filter = ('unit', 'service_charge', 'is_paid')
    search_fields = ('unit.name', 'service_charge.title')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('is_active',)
    ordering = ('title',)
    search_fields = ('title',)


admin.site.register(Building, BuildingAdmin)
admin.site.register(RequestPayment, RequestPaymentAdmin)
admin.site.register(VipService, VipServiceAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(ServiceCharge, ServiceChargeAdmin)
admin.site.register(ServiceChargeStatus, ServiceChargeStatusAdmin)
