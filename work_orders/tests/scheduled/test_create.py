from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
import logging

from work_orders.models import (
    ScheduledWorkOrder,
    ScheduledEventChoices,
    IntervalChoices,
)
from work_orders.forms import ScheduledWorkOrderForm
from equipment.models import (
    Equipment,
    HealthFacility,
    Manufacturer,
    Category,
    ServiceProvider,
    Department,
    EquipmentLocation,
)
from equipment.forms import EquipmentCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

logger = logging.getLogger(__name__)


class CreateScheduledWorkOrderViewTest(TestCase):
    def setUp(self):
        # Create test client and user
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

        # Create test Equipment
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

        self.url = reverse(
            "create_scheduled_work_order", args=[self.equipment.asset_tag]
        )

    def test_get_create_scheduled_work_order_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)

        # Log response
        logger.info("GET Response status code: %s", response.status_code)
        logger.info("GET Response content:\n%s", response.content.decode())

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "work_orders/create_scheduled_work_order.html"
        )
        self.assertIn("work_order_form", response.context)
        self.assertIn("equipment_form", response.context)
        self.assertIsInstance(
            response.context["work_order_form"], ScheduledWorkOrderForm
        )
        self.assertIsInstance(response.context["equipment_form"], EquipmentCreationForm)
        self.assertEqual(response.context["equipment_form"].instance, self.equipment)

    def test_post_create_scheduled_work_order_valid_data(self):
        self.client.force_login(self.user)
        valid_data = {
            "scheduled_action": ScheduledEventChoices.Preventive_Maintenance,
            "purchase_order": "1001",
            "freq_interval": IntervalChoices.Monthly,
            "frequency": "1",
            "next_scheduled_action_date": (
                timezone.now() + timezone.timedelta(days=30)
            ).date(),
            "last_serviced_at":"2024-03-27",
            "work_order_num":87987987
        }

        response = self.client.post(self.url, data=valid_data)

        # Log response
        logger.info("POST Response status code: %s", response.status_code)
        logger.info("POST Response content:\n%s", response.content.decode())

        # Assertions
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("scheduled_work_orders"))
        self.assertEqual(ScheduledWorkOrder.objects.count(), 1)

        work_order = ScheduledWorkOrder.objects.first()
        self.assertEqual(work_order.equipment, self.equipment)
        self.assertEqual(work_order.scheduled_action, valid_data["scheduled_action"])
        self.assertEqual(work_order.purchase_order, int(valid_data["purchase_order"]))
        self.assertEqual(work_order.freq_interval, valid_data["freq_interval"])
        self.assertEqual(
            work_order.next_scheduled_action_date,
            valid_data["next_scheduled_action_date"],
        )


