from django.contrib import admin
from .models import Building, Unit,Category
from django.utils.html import format_html


class BuildingAdmin(admin.ModelAdmin):
    list_display = ('building_id', 'name', 'image_tag', 'is_vip')
    ordering = ('name',)
    search_fields = ('name',)

    def image_tag(self, obj):
        return format_html(f'<img src="{obj.image.url}" with="25px" height="25px"/>')

    image_tag.short_description = True


class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'building', 'is_manager')
    search_fields = ('name', 'building')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('is_active',)
    ordering = ('title',)
    search_fields = ('title',)


admin.site.register(Building, BuildingAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Category, CategoryAdmin)
