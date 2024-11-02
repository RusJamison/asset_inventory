
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from equipment.models import Equipment, Department, HealthFacility, EquipmentLocation, Manufacturer, Category, ServiceProvider

class EquipmentDeleteViewTest(TestCase):
    def setUp(self):
        # Create a test user and log them in
        self.user = get_user_model().objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

        # Create required related instances
        self.manufacturer = Manufacturer.objects.create(name="Medical Supplies Inc.")
        self.category = Category.objects.create(name="Medical Devices")
        self.health_facility = HealthFacility.objects.create(name="City Hospital")
        self.service_provider = ServiceProvider.objects.create(name="TechCare Solutions")
        self.department = Department.objects.create(name="Radiology", health_facility=self.health_facility)

        # Create an EquipmentLocation and Equipment instance
        self.location = EquipmentLocation.objects.create(
            health_facility=self.health_facility,
            department=self.department,
        )
        
        self.equipment = Equipment.objects.create(
            name="MRI Machine",
            model="Model MRI-X200",
            asset_tag=1001,
            serial_no="MRI123456",
            description="High-resolution MRI machine",
            price=150000.00,
            manufacturer=self.manufacturer,
            status="IN_USE",
            purchase_order_number="PO10001",
            category=self.category,
            location=self.location,
            warranty_start_date="2022-01-01",
            warranty_end_date="2025-01-01",
            in_use_as_of_date="2022-01-15",
            service_provider=self.service_provider,
        )

    def test_delete_equipment_get(self):
        url = reverse("delete_equipment", args=[self.equipment.asset_tag])
        response = self.client.get(url)

        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Verify that the correct template is used
        self.assertTemplateUsed(response, "equipment/delete.html")

        # Check that the equipment instance is in the context
        self.assertIn("equipment", response.context)
        self.assertEqual(response.context["equipment"], self.equipment)

    def test_delete_equipment_post(self):
        url = reverse("delete_equipment", args=[self.equipment.asset_tag])

        # Send a POST request to delete the equipment
        response = self.client.post(url)

        # Check if the equipment was deleted
        self.assertFalse(Equipment.objects.filter(asset_tag=self.equipment.asset_tag).exists())

        # Verify that the view redirects to the equipment list
        self.assertRedirects(response, reverse("equipment_list"))