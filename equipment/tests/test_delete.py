# tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

from equipment.models import (
    Equipment,
    EquipmentLocation,
    HealthFacility,
    Manufacturer,
    Category,
    ServiceProvider,
    Department,
)

User = get_user_model()


class DeleteEquipmentViewTest(TestCase):
    def setUp(self):
        self.health_facility = HealthFacility.objects.create(
            name="Test Health Facility"
        )
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password",
            health_facility=self.health_facility,
        )

        self.user.is_verified = True
        self.user.save()

        self.manufacturer = Manufacturer.objects.create(name="Test Manufacturer")
        self.category = Category.objects.create(name="Test Category")
        self.service_provider = ServiceProvider.objects.create(
            name="Test Service Provider"
        )
        self.department = Department.objects.create(
            name="Test Department", health_facility=self.health_facility
        )

        self.location = EquipmentLocation.objects.create(
            health_facility=self.health_facility,
            department=self.department,
        )

        self.equipment = Equipment.objects.create(
            name="Test Equipment",
            model="Model X",
            asset_tag=12345,
            serial_no="SN12345",
            description="Test equipment description",
            price=1000.00,
            manufacturer=self.manufacturer,
            category=self.category,
            location=self.location,
            warranty_start_date="2023-01-01",
            warranty_end_date="2024-01-01",
            in_use_as_of_date="2023-01-15",
            service_provider=self.service_provider,
            status="in use",
            purchase_order_number="PO1234",
        )

    def test_delete_equipment_view_get_authenticated(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(
            reverse("delete_equipment", args=[self.equipment.asset_tag])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "equipment/delete.html")
        self.assertEqual(response.context["equipment"], self.equipment)

    def test_delete_equipment_view_get_unauthenticated(self):
        response = self.client.get(
            reverse("delete_equipment", args=[self.equipment.asset_tag])
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)

    def test_delete_equipment_view_post_authenticated(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(
            reverse("delete_equipment", args=[self.equipment.asset_tag])
        )
        equipment_exists = Equipment.objects.filter(
            asset_tag=self.equipment.asset_tag
        ).exists()
        self.assertFalse(equipment_exists)
        self.assertRedirects(response, reverse("equipment_list"))

    def test_delete_equipment_view_post_unauthenticated(self):
        response = self.client.post(
            reverse("delete_equipment", args=[self.equipment.asset_tag])
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)
        equipment_exists = Equipment.objects.filter(
            asset_tag=self.equipment.asset_tag
        ).exists()
        self.assertTrue(equipment_exists)

 
    
