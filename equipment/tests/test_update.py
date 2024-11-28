# tests.py

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
import logging

from equipment.models import (
    Equipment,
    Department,
    HealthFacility,
    EquipmentLocation,
    Manufacturer,
    Category,
    ServiceProvider,
)

logger = logging.getLogger(__name__)


class UpdateEquipmentViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.initial_facility = HealthFacility.objects.create(
            name="Initial Facility", location="City A"
        )
        self.category = Category.objects.create(name="Category 1")

        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="password",
            email="test@gmail.com",
            health_facility=self.initial_facility,
        )
        self.user.is_verified = True
        self.user.save()

        self.initial_department = Department.objects.create(
            name="Initial Department", health_facility=self.initial_facility
        )

        self.equipment_location = EquipmentLocation.objects.create(
            health_facility=self.initial_facility,
            department=self.initial_department,
        )
        self.manufacturer = Manufacturer.objects.create(name="Manufacturer 1")

        self.service_provider = ServiceProvider.objects.create(
            name="Service Provider 1"
        )

        self.equipment = Equipment.objects.create(
            name="Diathermy",
            model="31293821093",
            asset_tag=9873908,
            serial_no=980980,
            description="Test equipment",
            price=1000.00,
            manufacturer=self.manufacturer,
            category=self.category,
            location=self.equipment_location,
            warranty_start_date="2023-01-01",
            warranty_end_date="2024-01-01",
            in_use_as_of_date="2023-01-01",
            service_provider=self.service_provider,
        )

        self.new_facility = HealthFacility.objects.create(
            name="New Facility", location="City B"
        )
        self.new_department = Department.objects.create(
            name="New Department", health_facility=self.new_facility
        )

        self.url = reverse("edit_equipment", args=[self.equipment.asset_tag])

    def test_get_update_equipment_view(self):
        response = self.client.get(self.url)
        logger.info("GET Response status code: %s", response.status_code)
        logger.info("GET Response content: %s", response.content.decode())

        self.assertEqual(response.status_code, 302)

    def test_post_update_equipment_valid_data(self):
        update_data = {
            "name": "Updated Equipment",
            "model": "Model B",
            "asset_tag": self.equipment.asset_tag,
            "serial_no": "SN002",
            "department": self.new_department.id,
            "facilities": self.new_facility.id,
            "price": 12000,
            "description": "description",
            "status": "in use",
            "service_provider": self.service_provider.id,
            "manufacturer": self.manufacturer.id,
            "category": self.category.id
        }

        response = self.client.post(self.url, data=update_data)

        self.assertEqual(response.status_code, 302)
