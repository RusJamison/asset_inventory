from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from equipment.models import Equipment, Department, HealthFacility, EquipmentLocation, Manufacturer, Category, ServiceProvider
import logging


logger = logging.getLogger(__name__)

class EquipmentDetailsViewTest(TestCase):
    def setUp(self):
        # Create a test user and log them in
        self.user = get_user_model().objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

        # Create required related instances
        self.facility = HealthFacility.objects.create(name="City Hospital")
        self.manufacturer = Manufacturer.objects.create(name="Medical Supplies Inc.")
        self.category = Category.objects.create(name="Medical Devices")
        self.health_facility = HealthFacility.objects.create(name="City Hospital")
        self.service_provider = ServiceProvider.objects.create(name="TechCare Solutions")
        self.department = Department.objects.create(name="Radiology",health_facility=self.health_facility)

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

    def test_equipment_details_view(self):
        # Generate the URL for the details view
        url = reverse("equipment_details", args=[self.equipment.asset_tag])

        # Make a GET request to the view
        response = self.client.get(url)

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Verify that the correct template is used
        self.assertTemplateUsed(response, "equipment/equipment_details.html")

        # Check if the equipment and facility data are correctly passed to the context
        self.assertIn("equipment", response.context)
        self.assertEqual(response.context["equipment"], self.equipment)
        self.assertIn("location", response.context)
        self.assertEqual(response.context["location"], self.location)

        # Check that the title in the context is correctly formatted
        expected_title = f"Equipment Details - {self.equipment.name}"
        self.assertEqual(response.context["title"], expected_title)


