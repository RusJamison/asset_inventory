from django.contrib import admin
from .models import (
    Equipment,
    Category,
    EquipmentLocation,
    Manufacturer,
    HealthFacility,
    Department,
    ServiceProvider,
)
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Equipment)
class EquipmentAdmin(SummernoteModelAdmin):
    list_display = ("asset_tag", "serial_no", "model", "name")
    search_fields = ["asset_tag", "name"]
    list_filter = ("created_at",)
    summernote_fields = ("notes", "description")


# Register your models here.

# admin.site.register(Equipment)
admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(HealthFacility)
admin.site.register(Department)
admin.site.register(ServiceProvider)
admin.site.register(EquipmentLocation)
