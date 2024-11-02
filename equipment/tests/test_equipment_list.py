from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from equipment.models import Equipment, Department, HealthFacility, EquipmentLocation, Manufacturer, Category, ServiceProvider
import logging


logger = logging.getLogger(__name__)

class EquipmentListViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpass")
        
        # Log the user in
        self.client.login(username="testuser", password="testpass")
        # Set up related data for ForeignKeys
        self.facility = HealthFacility.objects.create(name="City Hospital")
        self.manufacturer = Manufacturer.objects.create(name="Medical Supplies Inc.")
        self.category = Category.objects.create(name="Medical Devices")
        self.health_facility = HealthFacility.objects.create(name="City Hospital")
        self.service_provider = ServiceProvider.objects.create(name="TechCare Solutions")
        self.department = Department.objects.create(name="Radiology",health_facility=self.health_facility)
        self.health_facility2 = HealthFacility.objects.create(name="Internal Hospital")
        self.department2 = Department.objects.create(name="Radiology",health_facility=self.health_facility)
        self.location = EquipmentLocation.objects.create(
            health_facility=self.health_facility,
            department=self.department,
        )

        self.location2 = EquipmentLocation.objects.create(
            health_facility=self.health_facility2,
            department=self.department2,
        )

        # Set up Equipment instances for medical equipment
        Equipment.objects.create(
            name="X-Ray Machine",
            model="Model XR200",
            asset_tag=1,
            serial_no="XR123456",
            description="High-resolution X-ray imaging device",
            price=75000.00,
            manufacturer=self.manufacturer,
            status="IN_USE",
            purchase_order_number="PO10001",
            category=self.category,
            warranty_start_date="2022-01-01",
            warranty_end_date="2025-01-01",
            in_use_as_of_date="2022-01-15",
            service_provider=self.service_provider,
            location = self.location
        )
        
        Equipment.objects.create(
            name="Ultrasound Machine",
            model="UltraSound-3000",
            asset_tag=2,
            serial_no="US789012",
            description="Portable ultrasound machine for diagnostic imaging",
            price=50000.00,
            manufacturer=self.manufacturer,
            status="IN_USE",
            purchase_order_number="PO10002",
            category=self.category,
            warranty_start_date="2022-02-01",
            warranty_end_date="2026-02-01",
            in_use_as_of_date="2022-02-15",
            service_provider=self.service_provider,
            location = self.location2
        )

    def test_equipment_list_view(self):
        response = self.client.get(reverse('equipment_list'))  

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the template used is correct
        self.assertTemplateUsed(response, "equipment/index.html")

        self.assertIn("equipments", response.context)
        self.assertEqual(len(response.context["equipments"]), 2)  # Should match the number of objects created in setUp

        # Check if specific attributes of the equipment are present in the context
        equipment_names = [equipment.name for equipment in response.context["equipments"]]
        self.assertIn("X-Ray Machine", equipment_names)
        self.assertIn("Ultrasound Machine", equipment_names)
