from django.db import models
from equipment.models import Equipment
from cloudinary.models import CloudinaryField
# Create your models here.

class ScheduledEventChoices(models.TextChoices):
    Preventive_Maintenance = "preventive_maintenance", "preventive_maintenance"
    Validation = "validation", "validation"
    Inspection = "inspection", "inspection"


class IntervalChoices(models.TextChoices):
    Daily = "daily", "daily"
    Weekly = "weekly", "weekly"
    Monthly = "monthly", "monthly"
    Yearly = "yearly", "yearly"


class ScheduledWorkOrder(models.Model):
    """Scheduled and expected"""
    work_order_num= models.IntegerField(unique=True,primary_key=True)
    equipment = models.ForeignKey(
        Equipment, on_delete=models.CASCADE, related_name="scheduled_events"
    )
    scheduled_action = models.CharField(
        max_length=200,
        choices=ScheduledEventChoices.choices,
        default="Preventive Maintenance",
    )
    purchase_order = models.IntegerField(null=True, blank=True)
    freq_interval = models.CharField(max_length=225,choices=IntervalChoices.choices, default="Yearly")
    last_serviced_at = models.DateField()
    next_scheduled_action_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"Work Order for equipment {self.equipment.asset_tag} NO {self.work_order_num}"

class WorkOrderType(models.TextChoices):
    Planned = "Planned", "Planned"
    Unplanned = "Unplanned", "Unplanned"

class WorKOrderStatus(models.TextChoices):
    Open = "Open", "Open"
    Closed = "Closed", "Closed"

class UnscheduledWorkOrder(models.Model):
    """Unplanned work on an equipment (abrupt)"""
    work_order_num = models.IntegerField(unique=True,primary_key=True)

    equipment = models.ForeignKey(
        Equipment, on_delete=models.CASCADE, related_name="unscheduled_work_orders"
    )
    problem = models.TextField()
    work_carried = models.CharField(max_length=200)
    work_order_report = CloudinaryField(resource_type="raw")
    purchase_order = models.IntegerField(null=True, blank=True, default=None)
    update = models.TextField()
    status = models.CharField(max_length=100, blank=True, choices= WorKOrderStatus.choices, default="Open")
    closed_at = models.DateTimeField(null=True, blank=True, default=None)
    date_of_update = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Work Order for equipment {self.equipment.asset_tag} NO {self.work_order_num}"

