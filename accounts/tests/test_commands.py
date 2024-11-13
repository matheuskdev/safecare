from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase

from departments.models import Department


class PopulateCommandTest(TestCase):
    """
    Tests for the 'populate' management command.
    This command populates the Department model and associates them with a specific user.
    """

    def setUp(self):
        """
        Create a user with ID 1 to ensure the command can associate departments with this user.
        """
        User = get_user_model()
        self.user = User.objects.create_user(
            username="admin", email="admin@example.com", password="password"
        )

    def test_populate_command(self):
        """
        Test that the 'populate' command runs without errors and creates the departments correctly.
        """
        call_command("populate")
        departments = Department.objects.all()
        self.assertEqual(departments.count(), 4)
        self.assertEqual(self.user.departments.count(), 4)
        self.assertTrue(self.user.departments.filter(name="TI").exists())

    def test_existing_departments(self):
        """
        Test that the 'populate' command does not recreate existing departments.
        """
        Department.objects.create(
            name="TI", description="Test Department", owner_id=1
        )
        call_command("populate")
        self.assertEqual(Department.objects.filter(name="TI").count(), 1)
