from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from equipment.models import Equipment, Manufacturer, Category, HealthFacility, Department, ServiceProvider, EquipmentLocation
from work_orders.models import ScheduledWorkOrder, UnscheduledWorkOrder

class CreateScheduledWorkOrderViewTest(TestCase):
    def setUp(self):
        # Create a test user and log them in
        self.user = get_user_model().objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

        # Set up related instances for Equipment
        manufacturer = Manufacturer.objects.create(name="Medical Supplies Inc.")
        category = Category.objects.create(name="Medical Devices")
        health_facility = HealthFacility.objects.create(name="City Hospital")
        department = Department.objects.create(name="Radiology", health_facility=health_facility)
        service_provider = ServiceProvider.objects.create(name="TechCare Solutions")

        # Create Equipment instance
        location = EquipmentLocation.objects.create(health_facility=health_facility, department=department)
        self.equipment = Equipment.objects.create(
            name="MRI Machine",
            model="Model MRI-X200",
            asset_tag=1001,
            serial_no="MRI123456",
            description="High-resolution MRI machine",
            price=150000.00,
            manufacturer=manufacturer,
            status="IN_USE",
            purchase_order_number="PO10001",
            category=category,
            location=location,
            warranty_start_date="2022-01-01",
            warranty_end_date="2025-01-01",
            in_use_as_of_date="2022-01-15",
            service_provider=service_provider,
        )

    def test_create_scheduled_work_order_get(self):
        url = reverse("create_scheduled_work_order", args=[self.equipment.asset_tag])
        response = self.client.get(url)

        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Verify that the correct template is used
        self.assertTemplateUsed(response, "work_orders/create_scheduled_work_order.html")

        # Check if both forms are in the context
        self.assertIn("work_order_form", response.context)
        self.assertIn("equipment_form", response.context)

    def test_create_scheduled_work_order_post(self):
        url = reverse("create_scheduled_work_order", args=[self.equipment.asset_tag])

        # Prepare valid POST data for ScheduledWorkOrderForm
        post_data = {
            "work_order_num": 1,
            "scheduled_action": "preventive_maintenance",
            "purchase_order": 12345,
            "freq_interval": "yearly",
           # "frequency": 1,
            "next_scheduled_action_date": "2024-12-01",
            "last_serviced_at": "2023-12-01",
        }

        # Send a POST request to create a scheduled work order
        response = self.client.post(url, post_data)

        # Check if the scheduled work order was created
        self.assertEqual(ScheduledWorkOrder.objects.count(), 1)
        work_order = ScheduledWorkOrder.objects.first()
        self.assertEqual(work_order.equipment, self.equipment)
        self.assertEqual(work_order.scheduled_action, "preventive_maintenance")
        self.assertEqual(work_order.purchase_order, 12345)

        # Verify that the view redirects to the scheduled work orders page
        self.assertRedirects(response, reverse("scheduled_work_orders"))