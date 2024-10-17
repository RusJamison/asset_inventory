from django.contrib import admin
from .models import Equipment, Category, Manufacturer, HealthFacility, Department, ServiceProvider

# Register your models here.

admin.site.register(Equipment)
admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(HealthFacility)
admin.site.register(Department)
admin.site.register(ServiceProvider)


