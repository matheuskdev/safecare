from django.db.utils import IntegrityError
from django.core.exceptions import FieldError

from departments.models import Department
from utils.test import SetUpInitial


class DepartmentModelTest(SetUpInitial):
    def setUp(self):
        super().setUp()

    def test_create_department(self):
        """Testa a criação de um departamento válido."""
        department = Department.objects.create(
            name='teste', description='teste descrição', owner_id=self.user.id
        )
        self.assertEqual(department.name, 'teste')
        self.assertEqual(department.description, 'teste descrição')
        self.assertEqual(department.owner_id, 1)

    def test_department_string_representation(self):
        """Testa o método __str__ do modelo."""
        department = Department.objects.get(id=1)
        self.assertEqual(str(department), department.name)

    def test_department_unique_name(self):
        """Testa a restrição de unicidade no campo 'name'."""
        with self.assertRaises(IntegrityError):
            Department.objects.create(name='Administração')

    def test_department_ordering(self):
        """Testa se o modelo é ordenado corretamente pelo campo 'name'."""
        d1 = Department.objects.get(name='Administração')
        d2 = Department.objects.get(name='TI')
        departments = Department.objects.all()
        self.assertEqual(list(departments), [d1, d2])

    def test_blank_description(self):
        """Testa a criação de um departamento com o campo 'description' em branco."""
        department = Department.objects.create(name='Financeiro', owner_id=self.user.id)
        self.assertEqual(department.description, None)

    def test_blank_name(self):
        """Testa a criação de um departamento com o campo 'name' em branco."""
        with self.assertRaises(FieldError):
            Department.objects.create(description='Financeiro', owner_id=self.user.id)
