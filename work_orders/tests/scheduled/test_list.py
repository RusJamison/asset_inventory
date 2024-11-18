from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from equipment.models import Equipment, EquipmentLocation, Manufacturer, Category, ServiceProvider, HealthFacility, Department

User = get_user_model()

class EquipmentListViewTest(TestCase):
    def setUp(self):
        """Set Up the tests"""
        self.health_facility = HealthFacility.objects.create(name='Health Facility 1')
        self.health_facility2 = HealthFacility.objects.create(name='Health Facility 2')

        self.manufacturer = Manufacturer.objects.create(name='Manufacturer 1')

        self.category = Category.objects.create(name='Category 1')

        self.service_provider = ServiceProvider.objects.create(name='Service Provider 1')

        self.department1 = Department.objects.create(name='X-Ray', health_facility=self.health_facility)
        self.department2 = Department.objects.create(name='X-Ray', health_facility=self.health_facility2)

        self.location1 = EquipmentLocation.objects.create(
            health_facility=self.health_facility,
            department = self.department1
        )


        self.location2 = EquipmentLocation.objects.create(
            health_facility=self.health_facility2,
            department = self.department2
        )


        Equipment.objects.create(
            name='Diathermy',
            model='31293821093',
            asset_tag=9873908,
            serial_no=980980,
            description='Test equipment',
            price=1000.00,
            manufacturer=self.manufacturer,
            category=self.category,
            location=self.location1,
            warranty_start_date='2023-01-01',
            warranty_end_date='2024-01-01',
            in_use_as_of_date='2023-01-01',
            service_provider=self.service_provider
        )

        Equipment.objects.create(
            name='Diathermy',
            model='31293821093',
            asset_tag=987354,
            serial_no=980980,
            description='Test equipment',
            price=1000.00,
            manufacturer=self.manufacturer,
            category=self.category,
            location=self.location2,
            warranty_start_date='2023-01-01',
            warranty_end_date='2024-01-01',
            in_use_as_of_date='2023-01-01',
            service_provider=self.service_provider
        )



        self.user = User.objects.create_user(username='testuser',email="test@gmail.com", password='password', health_facility=self.health_facility)
        self.user.health_facility = self.health_facility
        self.user.is_verified = True
        self.user.is_active = True
        self.user.save()

        self.superuser = User.objects.create_superuser(username='admin', password='adminpass',email="admin@gmail.com",  health_facility=self.health_facility)

    def test_equipment_list_view_with_superuser(self):
        """Test equipment list view with superuser"""
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('equipment_list'))

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.context['page_obj']), 2)  # Since pagination is set to 5
        self.assertEqual(response.context['page_obj'].paginator.count, 2)

        self.assertTemplateUsed(response, 'equipment/index.html')

    def test_equipment_list_view_with_regular_user(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('equipment_list'))

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.context['page_obj']), 1)  # Pagination
        self.assertEqual(response.context['page_obj'].paginator.count, 1)

        for equipment in response.context['page_obj']:
            self.assertEqual(equipment.location.health_facility, self.user.health_facility)

        self.assertTemplateUsed(response, 'equipment/index.html')

    def test_equipment_list_view_redirects_for_anonymous_user(self):
        response = self.client.get(reverse('equipment_list'))

        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

