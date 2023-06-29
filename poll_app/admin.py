from django.contrib import admin
from .models import Poll, PollOption

# Register your models here.

class PollAdmin(admin.ModelAdmin):
    list_display = ['building', '__str__', 'created']
    list_filter = ['building']
    ordering = ['-created']
    search_fields = ['building', '__str__']


class PollOptionAdmin(admin.ModelAdmin):
    list_display = ['poll', '__str__']
    list_filter = ['poll']
    search_fields = ['poll', '__str__']


admin.site.register(Poll, PollAdmin)
admin.site.register(PollOption, PollOptionAdmin)
