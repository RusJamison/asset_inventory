from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from equipment.models import  Equipment, Manufacturer, Category, HealthFacility, Department, ServiceProvider, EquipmentLocation
from work_orders.models import UnscheduledWorkOrder

class UnscheduledWorkOrdersViewTest(TestCase):
    def setUp(self):
        # Create a test user and log them in
        self.user = get_user_model().objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

        # Create necessary related instances for Equipment
        manufacturer = Manufacturer.objects.create(name="Medical Supplies Inc.")
        category = Category.objects.create(name="Medical Devices")
        health_facility = HealthFacility.objects.create(name="City Hospital")
        department = Department.objects.create(name="Radiology", health_facility=health_facility)
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
            status="in use",
            purchase_order_number="PO10001",
            category=category,
            location=location,
            warranty_start_date="2022-01-01",
            warranty_end_date="2025-01-01",
            in_use_as_of_date="2022-01-15",
            service_provider=service_provider,
        )

        # Create sample UnscheduledWorkOrder instances
        UnscheduledWorkOrder.objects.create(
            work_order_num=1,
            equipment=equipment,
            problem="Faulty display",
            work_carried="Replaced display screen",
            purchase_order=12345,
            update="Screen replaced successfully",
            status="Closed",
            closed_at="2024-01-10 10:00:00",
            date_of_update="2024-01-10",
        )
        UnscheduledWorkOrder.objects.create(
            work_order_num=2,
            equipment=equipment,
            problem="Overheating issue",
            work_carried="Cleaned and checked cooling system",
            purchase_order=67890,
            update="Cooling system cleaned; awaiting further inspection",
            status="Open",
            date_of_update="2024-01-15",
        )

    def test_unscheduled_work_orders_view(self):
        url = reverse("unscheduled_work_orders")  # Replace with your actual URL name for the view
        response = self.client.get(url)

        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Verify that the correct template is used
        self.assertTemplateUsed(response, "work_orders/unscheduled_work_orders.html")

        # Check that the context contains the unscheduled work orders
        self.assertIn("work_orders", response.context)
        self.assertEqual(len(response.context["work_orders"]), 2)  # Should match the number of objects created in setUp

        # Optional: Check specific attributes of the work orders to confirm they match
        work_order_problems = [work_order.problem for work_order in response.context["work_orders"]]
        self.assertIn("Faulty display", work_order_problems)
        self.assertIn("Overheating issue", work_order_problems)
        
        work_order_statuses = [work_order.status for work_order in response.context["work_orders"]]
        self.assertIn("Closed", work_order_statuses)
        self.assertIn("Open", work_order_statuses)
