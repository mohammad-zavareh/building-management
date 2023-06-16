from django.contrib import admin
from django.utils.html import format_html

from .models import Building, Unit

class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'is_vip')
    ordering = ('name',)
    search_fields = ('name',)

    def image_tag(self, obj):
        return format_html(f'<img src="{obj.image.url}" with="25px" height="25px"/>')

    image_tag.short_description = True


class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'building')
    search_fields = ('name', 'building')



admin.site.register(Building, BuildingAdmin)
admin.site.register(Unit, UnitAdmin)

