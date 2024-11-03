from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from equipment.models import Equipment, Manufacturer, Category, HealthFacility, Department, ServiceProvider, EquipmentLocation
from work_orders.models import ScheduledWorkOrder, UnscheduledWorkOrder

class ScheduledWorkOrdersViewTest(TestCase):
    def setUp(self):
        # Create a test user and log them in
        self.user = get_user_model().objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

        # Create necessary related instances for Equipment
        manufacturer = Manufacturer.objects.create(name="Medical Supplies Inc.")
        category = Category.objects.create(name="Medical Devices")
        health_facility = HealthFacility.objects.create(name="City Hospital")
        department = Department.objects.create(name="Radiology",health_facility=health_facility)
        service_provider = ServiceProvider.objects.create(name="TechCare Solutions")

        # Create Equipment instance
        location = EquipmentLocation.objects.create(health_facility=health_facility, department=department)
        equipment = Equipment.objects.create(
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

        # Create ScheduledWorkOrder instances
        ScheduledWorkOrder.objects.create(
            work_order_num=1,
            equipment=equipment,
            scheduled_action="Preventive Maintenance",
            purchase_order=12345,
            freq_interval="Yearly",
            #frequency=1,
            next_scheduled_action_date="2024-12-01",
            last_serviced_at="2023-12-01",
        )
        ScheduledWorkOrder.objects.create(
            work_order_num=2,
            equipment=equipment,
            scheduled_action="Inspection",
            purchase_order=67890,
            freq_interval="Monthly",
            #frequency=12,
            next_scheduled_action_date="2024-12-15",
            last_serviced_at="2024-11-15",
        )

    def test_scheduled_work_orders_view(self):
        url = reverse("scheduled_work_orders")  # Replace with your actual URL name for the view
        response = self.client.get(url)

        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Verify that the correct template is used
        self.assertTemplateUsed(response, "work_orders/scheduled_work_orders.html")

        # Check that the context contains the scheduled work orders
        self.assertIn("work_orders", response.context)
        self.assertEqual(len(response.context["work_orders"]), 2)  # Should match the number of objects created in setUp

        # Check specific attributes of the work orders
        work_order_numbers = [work_order.work_order_num for work_order in response.context["work_orders"]]
        self.assertIn(1, work_order_numbers)
        self.assertIn(2, work_order_numbers)
