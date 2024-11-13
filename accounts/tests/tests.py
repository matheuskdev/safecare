from io import StringIO

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.management import call_command
from django.test import TestCase

from departments.models import Department


class PopulateCommandTest(TestCase):
    """
    Test cases for the 'populate' management command, which populates the Department table
    and associates departments with a specific user.
    """

    def setUp(self):
        """
        Set up a user with ID 1 for testing department association.
        """
        User = get_user_model()

        self.user = User.objects.create_user(
            id=1,
            username="admin",
            email="admin@example.com",
            password="testpass",
        )

    def test_departments_creation(self):
        """
        Test that the 'populate' command creates the predefined departments successfully
        and verifies that the correct output is displayed.
        """
        out = StringIO()
        call_command("populate", stdout=out)

        departments = Department.objects.all()
        self.assertEqual(departments.count(), 4)

        output = out.getvalue()
        self.assertIn(
            'Department " Administração" created successfully!', output
        )
        self.assertIn('Department "Financeiro" created successfully!', output)
        self.assertIn(
            'Department "Recursos Humanos" created successfully!', output
        )
        self.assertIn('Department "TI" created successfully!', output)

    def test_user_association_with_departments(self):
        """
        Test that the 'populate' command associates the user with all created departments.
        """
        out = StringIO()
        call_command("populate", stdout=out)

        user = get_user_model().objects.get(id=1)
        departments = Department.objects.all()
        self.assertEqual(user.departments.count(), departments.count())

        output = out.getvalue()
        self.assertIn(
            "Departments associated with the user successfully!", output
        )

    def test_existing_department(self):
        """
        Test that the 'populate' command handles existing departments correctly
        and does not recreate them, displaying the appropriate message.
        """

        Department.objects.create(
            name=" Administração",
            description="Departamento Administrativo",
            owner_id=1,
        )

        out = StringIO()
        call_command("populate", stdout=out)

        output = out.getvalue()
        self.assertIn('Department " Administração" already exists.', output)

    def test_no_user_found(self):
        """
        Test that the 'populate' command raises an exception if the user with ID 1 is not found.
        """
        get_user_model().objects.filter(id=1).delete()

        out = StringIO()

        with self.assertRaises(get_user_model().DoesNotExist):
            call_command("populate", stdout=out)

    def test_user_with_short_username(self):
        """Test creating a user with a username shorter than 4 characters raises an error."""
        with self.assertRaises(ValidationError):
            user = self.User(
                username="abc",
                email="user@example.com",
                password="password123",
            )
            user.full_clean()

    def test_user_str_method(self):
        """Test the __str__ method returns the user's email."""
        user = self.User.objects.create_user(
            username="testuser",
            email="user@example.com",
            password="password123",
        )
        self.assertEqual(str(user), "user@example.com")

    def test_user_optional_fields(self):
        """Test creating a user with optional fields."""
        user = self.User.objects.create_user(
            username="testuser",
            email="user@example.com",
            password="password123",
            first_name="Test",
            last_name="User",
            bio="This is a test bio.",
            website="https://example.com",
        )
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")
        self.assertEqual(user.bio, "This is a test bio.")
        self.assertEqual(user.website, "https://example.com")

    def test_user_department_association(self):
        """Test associating a user with multiple departments."""
        department1 = Department.objects.create(
            name="Department 1", description="Desc 1"
        )
        department2 = Department.objects.create(
            name="Department 2", description="Desc 2"
        )
        user = self.User.objects.create_user(
            username="testuser",
            email="user@example.com",
            password="password123",
        )
        user.departments.add(department1, department2)
        self.assertEqual(user.departments.count(), 2)
        self.assertIn(department1, user.departments.all())
        self.assertIn(department2, user.departments.all())

    def test_create_user_without_email(self):
        """Test that creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError) as context:
            # Tenta criar um usuário com o email vazio
            self.User.objects.create_user(email="", password="password123")

        # Verifica se a mensagem de erro é a esperada
        self.assertEqual(
            str(context.exception), "O campo de email deve ser preenchido."
        )
