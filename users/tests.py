from django.test import TestCase
from users.models import CustomUser as User
from equipment.models import HealthFacility
import logging

logger = logging.getLogger(__name__)


class UserTestCase(TestCase):
    def setUp(self):
        self.health_facility = HealthFacility.objects.create(
            name="Test Hospital")
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass",
            health_facility=self.health_facility
        )

    def test_create_user(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertTrue(self.user.is_active)
        self.assertEqual(self.user.health_facility, self.health_facility)

    def test_login(self):
        logged_in = self.client.login(username="testuser", password="testpass")
        self.assertTrue(logged_in)
        self.assertTrue(self.user.is_active)
        logger.info("User is active ".format())
