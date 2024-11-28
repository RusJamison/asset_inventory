# tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
# Import your models
from equipment.models import (
    Equipment,
    EquipmentLocation,
    HealthFacility,
    Manufacturer,
    Category,
    ServiceProvider,
    Department
)

User = get_user_model()


class EquipmentDetailsViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.health_facility = HealthFacility.objects.create(
             name='Test Health Facility')
        self.user = User.objects.create_user(
            username='testuser', password='password',
            email="testuser@example.com",
            health_facility=self.health_facility
         )
        self.user.is_verified = True
        self.user.save()

        self.manufacturer = Manufacturer.objects.create(
            name='Test Manufacturer')
        self.category = Category.objects.create(name='Test Category')
        self.service_provider = ServiceProvider.objects.create(
             name='Test Service Provider')
        self.department = Department.objects.create(
             name="Radiology",
             health_facility=self.health_facility
        )

        self.location = EquipmentLocation.objects.create(
            health_facility=self.health_facility,
            department=self.department
        )

        # Create an Equipment instance
        self.equipment = Equipment.objects.create(
            name='Test Equipment',
            model='Model X',
            asset_tag=12345,  # Primary key
            serial_no='SN12345',
            description='Test equipment description',
            price=1000.00,
            manufacturer=self.manufacturer,
            category=self.category,
            location=self.location,
            warranty_start_date='2023-01-01',
            warranty_end_date='2024-01-01',
            in_use_as_of_date='2023-01-15',
            service_provider=self.service_provider,
            status='in use',
            purchase_order_number='PO1234',
        )

    def test_equipment_details_view_authenticated_user(self):
        # Log in the user
        self.client.login(username='testuser', password='password')

        response = self.client.get(reverse(
            'equipment_details',
            args=[self.equipment.asset_tag]
            ))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'equipment/equipment_details.html')

        self.assertEqual(response.context['equipment'], self.equipment)
        self.assertEqual(response.context['location'], self.equipment.location)
        self.assertEqual(response.context['title'],
                         f"Equipment Details - {self.equipment.name}")

    def test_equipment_details_view_unauthenticated_user(self):

        response = self.client.get(reverse('equipment_details',
                                           args=[self.equipment.asset_tag]))

        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)
