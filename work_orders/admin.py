from django.contrib import admin
from .models import ScheduledWorkOrder, UnscheduledWorkOrder
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(ScheduledWorkOrder)
admin.site.register(UnscheduledWorkOrder)
