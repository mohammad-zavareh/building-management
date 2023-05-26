from django.contrib import admin

from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'building',)
    list_filter = ('building',)
    ordering = ('-created',)
    search_fields = ('title',)

admin.site.register(Notification, NotificationAdmin)