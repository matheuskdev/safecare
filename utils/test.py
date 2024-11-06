from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from departments.models import Department


class SetUpInitial(TestCase):
    """
    Setup class for initializing test environment with users, departments, and permissions.

    This class creates a test user, adds predefined departments, and logs in 
    the user for use in subsequent test cases. It also provides a helper method 
    to assign permissions to the user dynamically.

    Attributes:
        User (User model): The custom user model used in the project.
        user (User instance): The test user created during setup.

    Methods:
        setUp(): Initializes the test environment with a user and departments.
        set_permission(model, codename): Assigns a permission to the user 
            for a given model and codename.
    """
    
    User = get_user_model()

    def setUp(self):
        """
        Set up the test environment.

        This method creates a test user, sets up initial departments, and 
        logs in the user. Departments are created using `get_or_create` 
        to avoid duplication, and the test user is assigned to the 
        'Administração' department.

        Side Effects:
            - Creates a new user in the database.
            - Creates or retrieves specified departments.
            - Logs the user in for client-based testing.
        """
        self.user = self.User.objects.create_user(
            email='testuser@123.com', password='password'
        )
        
        departments = [
            {
                'name': 'Administração',
                'description': 'Departamento Administrativo',
            },
            {
                'name': 'TI',
                'description': 'Departamento de Tecnologia da Informação',
            },
        ]

        for dept_data in departments:
            department, created = Department.objects.get_or_create(
                name=dept_data['name'],
                defaults={
                    'description': dept_data['description'],
                    'owner_id': 1,
                },
            )
        self.user.departments.add(Department.objects.get(id=1))
        self.client.login(email='testuser@123.com', password='password')

    def set_permission(self, model, codename):
        """
        Assign a permission to the test user for a given model.

        This method dynamically assigns a permission to the test user 
        based on the provided model and permission codename.

        Args:
            model (Model): The model for which the permission is assigned.
            codename (str): The codename of the permission.

        Side Effects:
            - Adds the specified permission to the user's permissions.
        """
        content_type = ContentType.objects.get_for_model(model)
        permission, created = Permission.objects.get_or_create(
            codename=codename, content_type=content_type
        )
        self.user.user_permissions.add(permission)
