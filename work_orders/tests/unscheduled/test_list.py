# # tests.py
# from django.test import TestCase, Client
# from django.urls import reverse
# from django.utils import timezone
# import logging
# from django.contrib.auth import get_user_model
# from work_orders.models import UnscheduledWorkOrder, WorKOrderStatus
# from equipment.models import (
#     Equipment,
#     EquipmentLocation,
#     ServiceProvider,
#     Manufacturer,
#     Department,
#     HealthFacility,
#     Category,
# )

# User = get_user_model()

# logger = logging.getLogger(__name__)


# class UnscheduledWorkOrdersViewTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.initial_facility = HealthFacility.objects.create(
#             name="Initial Facility", location="City A"
#         )
#         self.initial_department = Department.objects.create(
#             name="Initial Department", health_facility=self.initial_facility
#         )
#         self.user = User.objects.create_user(
#             username="testuser",
#             email="testuser@example.com",
#             password="password",
#             health_facility=self.initial_facility,
#         )

#         self.user.is_verified = True
#         self.user.save()
#         self.equipment_location = EquipmentLocation.objects.create(
#             health_facility=self.initial_facility,
#             department=self.initial_department,
#         )
#         self.category = Category.objects.create(name="Category 1")


#         self.manufacturer = Manufacturer.objects.create(name="Manufacturer 1")

#         self.service_provider = ServiceProvider.objects.create(
#             name="Service Provider 1"
#         )

#         self.equipment = Equipment.objects.create(
#             name="Diathermy",
#             model="31293821093",
#             asset_tag=9873908,
#             serial_no=980980,
#             description="Test equipment",
#             price=1000.00,
#             manufacturer=self.manufacturer,
#             category=self.category,
#             location=self.equipment_location,
#             warranty_start_date="2023-01-01",
#             warranty_end_date="2024-01-01",
#             in_use_as_of_date="2023-01-01",
#             service_provider=self.service_provider,
#         )

#         # Create test UnscheduledWorkOrders
#         self.work_order1 = UnscheduledWorkOrder.objects.create(
#             work_order_num=1001,
#             equipment=self.equipment,
#             problem="The display screen is flickering intermittently.",
#             work_carried="Replaced the display screen.",
#             purchase_order=5001,
#             update="Screen replaced and tested successfully.",
#             status=WorKOrderStatus.Closed,
#             closed_at=timezone.now(),
#             date_of_update=timezone.now().date(),
#         )

#         self.work_order2 = UnscheduledWorkOrder.objects.create(
#             work_order_num=1002,
#             equipment=self.equipment,
#             problem="Machine is overheating after 2 hours of continuous use.",
#             work_carried="Cleaned the cooling vents and replaced the fan.",
#             purchase_order=5002,
#             update="Overheating issue resolved.",
#             status=WorKOrderStatus.Open,
#             date_of_update=timezone.now().date(),
#         )

#         self.work_order3 = UnscheduledWorkOrder.objects.create(
#             work_order_num=1003,
#             equipment=self.equipment,
#             problem="Error code E05 displayed during startup.",
#             work_carried="Diagnosed faulty power supply unit.",
#             purchase_order=5003,
#             update="Awaiting delivery of new power supply unit.",
#             status=WorKOrderStatus.Open,
#             date_of_update=timezone.now().date(),
#         )

#         self.url = reverse("unscheduled_work_orders")

#     def test_unscheduled_work_orders_view(self):
#         self.client.force_login(self.user)
#         response = self.client.get(self.url)

#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "work_orders/unscheduled_work_orders.html")
#         self.assertIn("work_orders", response.context)
#         self.assertEqual(response.context["title"], "Unscheduled Work Orders")

#     def test_unscheduled_work_orders_view_no_work_orders(self):
#         self.client.force_login(self.user)
#         UnscheduledWorkOrder.objects.all().delete()

#         response = self.client.get(self.url)

#         logger.info(
#             "Response with no work orders status code: %s", response.status_code
#         )
#         logger.info(
#             "Response content with no work orders:\n%s", response.content.decode()
#         )

#         self.assertEqual(response.status_code, 200)

#         self.assertQuerySetEqual(response.context["work_orders"], [])
