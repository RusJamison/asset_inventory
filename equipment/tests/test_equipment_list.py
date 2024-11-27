from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from equipment.models import (
    Equipment,
    Manufacturer,
    Category,
    HealthFacility,
    Department,
    ServiceProvider,
    EquipmentLocation
)
from work_orders.models import ScheduledWorkOrder, UnscheduledWorkOrder
from datetime import date


class EquipmentListViewTest(TestCase):
    def setUp(self):

        self.client = Client()

        self.health_facility_1 = HealthFacility.objects.create(
            name="City Hospital")
        self.health_facility_2 = HealthFacility.objects.create(
            name="County Clinic")

        User = get_user_model()
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass",
            health_facility=self.health_facility_1
        )

        self.user.is_verified = True
        self.user.save()
        self.superuser = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="adminpass",
            health_facility=self.health_facility_1
        )

        self.client.login(username="testuser", password="testpass")
        self.manufacturer = Manufacturer.objects.create(
            name="Medical Supplies Inc.")
        self.category = Category.objects.create(name="Medical Devices")
        self.department = Department.objects.create(
            name="Radiology",
            health_facility=self.health_facility_1
        )
        self.service_provider = ServiceProvider.objects.create(
            name="TechCare Solutions")

        self.location_1 = EquipmentLocation.objects.create(
            health_facility=self.health_facility_1,
            department=self.department,
        )
        self.location_2 = EquipmentLocation.objects.create(
            health_facility=self.health_facility_2,
            department=self.department,
        )

        self.equipment1 = Equipment.objects.create(
            name="X-Ray Machine",
            model="XR-200",
            asset_tag=1002,
            serial_no="XR123456",
            description="Standard X-Ray Machine",
            price=50000.00,
            manufacturer=self.manufacturer,
            status="IN_USE",
            purchase_order_number="PO10002",
            category=self.category,
            location=self.location_1,
            warranty_start_date=date(2023, 1, 1),
            warranty_end_date=date(2026, 1, 1),
            in_use_as_of_date=date(2023, 1, 15),
            service_provider=self.service_provider,
        )
        self.equipment2 = Equipment.objects.create(
            name="Ultrasound Machine",
            model="US-300",
            asset_tag=1003,
            serial_no="US123456",
            description="High-frequency Ultrasound Machine",
            price=75000.00,
            manufacturer=self.manufacturer,
            status="IN_USE",
            purchase_order_number="PO10003",
            category=self.category,
            location=self.location_2,  # Assign to location_2
            warranty_start_date=date(2023, 6, 1),
            warranty_end_date=date(2026, 6, 1),
            in_use_as_of_date=date(2023, 6, 15),
            service_provider=self.service_provider,
        )

    def test_equipment1_assigned_to_location1(self):
        self.assertEqual(self.equipment1.location, self.location_1)
        self.assertEqual(
            self.equipment1.location.health_facility, self.health_facility_1)

    def test_equipment2_assigned_to_location2(self):
        self.assertEqual(self.equipment2.location, self.location_2)
        self.assertEqual(
                         self.equipment2.location.health_facility,
                         self.health_facility_2
                         )

    def test_equipment_list_view_as_regular_user(self):
        # Log in as a regular user
        login = self.client.login(username="testuser", password="testpass")
        self.assertTrue(login)

        url = reverse("equipment_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "equipment/index.html")

        equipment_list = response.context['page_obj'].object_list
        self.assertIn(self.equipment1, equipment_list)
        self.assertNotIn(self.equipment2, equipment_list)

    def test_equipment_list_view_as_superuser(self):

        self.client.force_login(self.superuser)

        url = reverse("equipment_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "equipment/index.html")

        equipment_list = response.context['page_obj'].object_list
        self.assertIn(self.equipment1, equipment_list)
        self.assertIn(self.equipment2, equipment_list)
