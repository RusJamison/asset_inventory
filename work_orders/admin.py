from django.contrib import admin
from .models import ScheduledWorkOrder, UnscheduledWorkOrder

# Register your models here.
admin.site.register(ScheduledWorkOrder)
admin.site.register(UnscheduledWorkOrder)
