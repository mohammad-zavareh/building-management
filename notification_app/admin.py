from django.contrib import admin

from .models import Notification, Comment


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'building',)
    list_filter = ('building',)
    ordering = ('-created',)
    search_fields = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'unit', 'notification',)
    list_filter = ('unit', 'notification',)
    ordering = ('-created',)
    search_fields = ('text',)


admin.site.register(Notification, NotificationAdmin)
admin.site.register(Comment, CommentAdmin)