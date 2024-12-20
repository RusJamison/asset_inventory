from django.db import models
from cloudinary.models import CloudinaryField


class StatusChoices(models.TextChoices):
    IN_USE = "in use", "in use"
    UNDER_REPAIR = "under repair", "under repair"
    AVAILABLE = "available", "available"
    DECOMMISIONED = "decommissioned", "decommissioned"


# Create your models here.
class Equipment(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=250)
    asset_tag = models.IntegerField(default=0, unique=True, primary_key=True)
    serial_no = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField(resource_type="image", null=True, blank=True,
                            default=None)
    notes = models.TextField(null=True, blank=True, default=None)
    manufacturer = models.ForeignKey(
        "Manufacturer", on_delete=models.CASCADE, related_name="equipments"
    )
    user_manual = CloudinaryField(
        resource_type="raw", null=True, blank=True, default=None
    )
    status = models.CharField(
        max_length=250, choices=StatusChoices.choices,
        default=StatusChoices.IN_USE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    purchase_order_number = models.CharField(max_length=50, blank=True)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="equipments"
    )
    location = models.OneToOneField(
        "EquipmentLocation", related_name="equipment", on_delete=models.CASCADE
    )
    warranty_start_date = models.DateField()
    warranty_end_date = models.DateField()
    in_use_as_of_date = models.DateField()
    service_provider = models.ForeignKey(
        "ServiceProvider", on_delete=models.CASCADE, related_name="equipments"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Equipment"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Manufacturer(models.Model):
    name = models.CharField(default="Company", max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Manufacturers"


class HealthFacility(models.Model):
    name = models.CharField(max_length=225)
    location = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Health Facilities"


class Department(models.Model):
    name = models.CharField(max_length=200)
    health_facility = models.ForeignKey(
        HealthFacility, on_delete=models.CASCADE, related_name="departments"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Departments"


class EquipmentLocation(models.Model):
    """Relates an equipment to a location and a department"""

    health_facility = models.ForeignKey(
        HealthFacility, related_name="equipment_location",
        on_delete=models.CASCADE
    )
    department = models.ForeignKey(
        Department, related_name="equipment_location", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.health_facility.name} and \
        departmet {self.department.name}"


class ServiceProvider(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Service Providers"
