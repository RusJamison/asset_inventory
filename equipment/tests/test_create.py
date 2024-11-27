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


class EquipmentCreateViewTest(TestCase):
    def setUp(self):
        # Create a test user and log them in

        # Create required related instances

        self.facility = HealthFacility.objects.create(name="City Hospital")
        User = get_user_model()
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass",
            health_facility=self.facility
        )

        self.user.is_verified = True
        self.user.save()
        self.manufacturer = Manufacturer.objects.create(
            name="Medical Supplies Inc.")
        self.category = Category.objects.create(name="Medical Devices")
        self.health_facility = HealthFacility.objects.create(
            name="City Hospital")
        self.service_provider = ServiceProvider.objects.create(
            name="TechCare Solutions"
        )
        self.department = Department.objects.create(
            name="Radiology", health_facility=self.health_facility
        )
        self.location = EquipmentLocation.objects.create(
            health_facility=self.health_facility,
            department=self.department,
        )

        self.url = reverse(
            "create_equipment"
        )  # Replace with your actual URL name for the create view

    def test_create_equipment_get(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the template used is correct
        self.assertTemplateUsed(response, "equipment/create.html")

        # Check that the form is in the context
        self.assertIn("form", response.context)

    def test_create_equipment_post_save_and_add(self):
        self.client.force_login(self.user)
        post_data = {
            "name": "MRI Machine",
            "model": "Model MRI-X200",
            "asset_tag": 4,
            "serial_no": "MRI654321",
            "description": "Portable MRI machine",
            "price": 120000.00,
            "department": self.department.id,
            "facilities": self.facility.id,
            "manufacturer": self.manufacturer.id,
            "notes": "some notes",
            "status": "in use",
            "category": self.category.id,
            "service_provider": self.service_provider.id,
            "warranty_start_date": "2022-01-01",
            "warranty_end_date": "2025-01-01",
            "in_use_as_of_date": "2022-01-15",
            "save_and_duplicate": "Save and Duplicate",
            "purchase_order_number": 12345678,
            "department_id": self.department.id,
            "facilities": self.health_facility.id,
        }

        response = self.client.post(self.url, post_data)

    def test_create_equipment_post_save_and_duplicate(self):
        self.client.force_login(self.user)
        post_data = {
            "name": "MRI Machine",
            "model": "Model MRI-X200",
            "asset_tag": 4,
            "serial_no": "MRI654321",
            "description": "Portable MRI machine",
            "price": 120000.00,
            "department": self.department.id,
            "facilities": self.facility.id,
            "manufacturer": self.manufacturer.id,
            "notes": "some notes",
            "status": "in use",
            "category": self.category.id,
            "service_provider": self.service_provider.id,
            "warranty_start_date": "2022-01-01",
            "warranty_end_date": "2025-01-01",
            "in_use_as_of_date": "2022-01-15",
            "save_and_duplicate": "Save and Duplicate",
            "purchase_order_number": 12345678,
        }

        response = self.client.post(self.url, post_data)
        '''
        Check if the response renders the form with prefilled data for
        duplication
        '''
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
        self.assertEqual(response.context["form"].initial["name"],
                         "MRI Machine")

    def test_create_equipment_post_save_and_redirect(self):
        self.client.force_login(self.user)
        post_data = {
            "name": "MRI Machine",
            "model": "Model MRI-X200",
            "asset_tag": 4,
            "serial_no": "MRI654321",
            "description": "Portable MRI machine",
            "price": 120000.00,
            "department": self.department.id,
            "facilities": self.facility.id,
            "manufacturer": self.manufacturer.id,
            "notes": "some notes",
            "status": "in use",
            "category": self.category.id,
            "service_provider": self.service_provider.id,
            "warranty_start_date": "2022-01-01",
            "warranty_end_date": "2025-01-01",
            "in_use_as_of_date": "2022-01-15",
            "save_and_duplicate": "Save and Duplicate",
            "purchase_order_number": 12345678,
        }

        response = self.client.post(self.url, post_data)
