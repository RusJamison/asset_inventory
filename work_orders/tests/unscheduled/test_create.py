from django.test import TestCase, Client
from django.urls import reverse
from work_orders.models import UnscheduledWorkOrder
from work_orders.forms import UnScheduleWorkOrderForm
from equipment.models import (
    Equipment,
    EquipmentLocation,
    Manufacturer,
    ServiceProvider,
    HealthFacility,
    Department,
    Category,
)
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model 


class UnscheduledWorkOrderViewTests(TestCase):
    def setUp(self):
        # Create a test user and log them in
        self.user = get_user_model().objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        manufacturer = Manufacturer.objects.create(name="Medical Supplies Inc.")
        category = Category.objects.create(name="Medical Devices")
        health_facility = HealthFacility.objects.create(name="City Hospital")
        department = Department.objects.create(
            name="Radiology", health_facility=health_facility
        )
        service_provider = ServiceProvider.objects.create(name="TechCare Solutions")

        location = EquipmentLocation.objects.create(
            health_facility=health_facility, department=department
        )
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

        self.unscheduled_work_orders_url = reverse("unscheduled_work_orders")
        self.create_work_order_url = reverse(
            "create_unscheduled_work_order", args=[self.equipment.asset_tag]
        )

    def test_create_unscheduled_work_order_view_post_valid(self):
        form_data = {
            "problem": "Test problem description",
            "work_carried": "Test work carried",
            "work_order_num": 123456,
            "purchase_order": 123456,
            "update": "2022-10-12",
            "status": "Open",
            "closed_at": "2022-10-11",
            "date_of_update": "2024-12-12",
        }
        response = self.client.post(self.create_work_order_url, data=form_data)
        self.assertEqual(UnscheduledWorkOrder.objects.count(), 1)
        work_order = UnscheduledWorkOrder.objects.first()
        self.assertEqual(work_order.equipment, self.equipment)
        self.assertEqual(work_order.problem, "Test problem description")

    def test_create_unscheduled_work_order_view_post_invalid(self):
        form_data = {}
        response = self.client.post(self.create_work_order_url, data=form_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "work_orders/create_unscheduled_work_order.html"
        )

        # Check if form errors are in the response context
        self.assertIn("work_order_form", response.context)
        form = response.context["work_order_form"]
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
