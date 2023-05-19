from django.contrib import admin

from .models import VipService


class VipServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'time', 'max_unit')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(VipService, VipServiceAdmin)