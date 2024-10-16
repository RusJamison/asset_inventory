from django.db import models


class StatusChoices(models.TextChoices):
    IN_USE = "in use", "in use"
    UNDER_REPAIR = "under repair", "under repair"
    AVAILABLE = "available", "available"
    DECOMMISIONED = "decommissioned", "decommissioned"


#class ManufacturerChoices(models.TextChoices):
#    COMPANY_A = "Company A", "Company A"
#    COMPANY_B = "Company B", "Company B"
#    COMPANY_C = "Company C", "Company C"


# Create your models here.
class Equipment(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=250)
    asset_tag = models.IntegerField(default=0, unique=True, primary_key=True)
    serial_no = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="equipment_images/", null=True, blank=True)
    notes = models.TextField(null=True)
    manufacturer = models.ForeignKey(
        "Manufacturer", on_delete=models.CASCADE, related_name="equipments"
    )
    user_manual = models.FileField(upload_to="equipment_images/")
    status = models.CharField(
        max_length=250, choices=StatusChoices.choices, default=StatusChoices.IN_USE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    purchase_order_number = models.CharField(max_length=50, blank=True)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="equipments"
    )
    health_facility = models.ForeignKey(
        "HealthFacility", on_delete=models.CASCADE, related_name="equipments"
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
   name = models.CharField(default='Company', max_length=200)
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


class ServiceProvider(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Service Providers"





