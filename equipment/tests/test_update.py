from equipment.models import (
    Equipment,
    EquipmentLocation,
    ServiceProvider,
    Department,
    Manufacturer,
    Category,
    HealthFacility,
)
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class EquipmentUpdateViewTest(TestCase):
    def setUp(self):
        # Create a test user and log them in
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpass"
        )
        self.client.login(username="testuser", password="testpass")

        # Create required related instances
        self.facility = HealthFacility.objects.create(name="City Hospital")
        self.manufacturer = Manufacturer.objects.create(name="Medical Supplies Inc.")
        self.category = Category.objects.create(name="Medical Devices")
        self.health_facility = HealthFacility.objects.create(name="City Hospital")
        self.service_provider = ServiceProvider.objects.create(
            name="TechCare Solutions"
        )
        self.department = Department.objects.create(
            name="Radiology", health_facility=self.health_facility
        )

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

        # Create additional department and facility for testing updates
        self.new_department = Department.objects.create(
            name="Cardiology", health_facility=self.health_facility
        )
        self.new_facility = HealthFacility.objects.create(name="General Hospital")

    def test_update_equipment_get(self):
        url = reverse("edit_equipment", args=[self.equipment.asset_tag])
        response = self.client.get(url)

        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Verify that the correct template is used
        self.assertTemplateUsed(response, "equipment/update.html")

        # Check if the form is pre-filled with the correct equipment data
        self.assertIn("form", response.context)
        self.assertEqual(response.context["form"].initial["name"], self.equipment.name)

    def test_update_equipment_post(self):
        url = reverse("edit_equipment", args=[self.equipment.asset_tag])

        # Prepare POST data to update equipment location and details
        post_data = {
            "name": "Updated MRI Machine",
            "model": "Updated Model MRI-X200",
            "serial_no": "MRI654321",
            "description": "Updated MRI machine description",
            "price": 175000.00,
            "department": self.new_department.id,
            "facility": self.new_facility.id,
            "manufacturer": self.manufacturer.id,
            "status": "IN_USE",
            "category": self.category.id,
            "service_provider": self.service_provider.id,
            "warranty_start_date": "2022-01-01",
            "warranty_end_date": "2025-01-01",
            "in_use_as_of_date": "2022-01-15",
            "department": self.new_department.id,
            "facility": self.new_facility.id,
            "status": "in use",
            "asset_tag": self.equipment.asset_tag,
        }

        # Send a POST request to update the equipment
        response = self.client.post(url, post_data)

        # Reload the equipment from the database
        self.equipment.refresh_from_db()

        # Check if the update was successful and redirected to the equipment list
        # self.assertRedirects(response, reverse("equipment_list"))

        # Verify that the equipment data and location have been updated
        self.assertEqual(self.equipment.name, "Updated MRI Machine")
        self.assertEqual(self.equipment.model, "Updated Model MRI-X200")
        self.assertEqual(self.equipment.location.department, self.new_department)
        self.assertEqual(self.equipment.location.health_facility, self.new_facility)
