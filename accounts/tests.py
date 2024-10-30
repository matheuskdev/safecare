from io import StringIO

import pytest
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase

from departments.models import Department


class PopulateCommandTest(TestCase):

    def setUp(self):
        # Cria um usuário com ID 1
        User = get_user_model()
        self.user = User.objects.create_user(
            id=1, username='admin', email='admin@example.com', password='testpass'
        )

    def test_departments_creation(self):
        # Captura a saída do comando
        out = StringIO()
        call_command('populate', stdout=out)

        # Verifica se os departamentos foram criados corretamente
        departments = Department.objects.all()
        self.assertEqual(departments.count(), 4)

        # Verifica as mensagens de sucesso e aviso
        output = out.getvalue()
        self.assertIn('Department " Administração" created successfully!', output)
        self.assertIn('Department "Financeiro" created successfully!', output)
        self.assertIn('Department "Recursos Humanos" created successfully!', output)
        self.assertIn('Department "TI" created successfully!', output)

    def test_user_association_with_departments(self):
        # Captura a saída do comando
        out = StringIO()
        call_command('populate', stdout=out)

        # Recupera o usuário de ID 1
        user = get_user_model().objects.get(id=1)

        # Verifica se o usuário foi associado a todos os departamentos
        departments = Department.objects.all()
        self.assertEqual(user.departments.count(), departments.count())

        # Verifica as mensagens de associação
        output = out.getvalue()
        self.assertIn("Departments associated with the user successfully!", output)

    def test_existing_department(self):
        # Cria manualmente um departamento existente
        Department.objects.create(name=" Administração", description="Departamento Administrativo", owner_id=1)

        # Captura a saída do comando
        out = StringIO()
        call_command('populate', stdout=out)

        # Verifica se a mensagem de aviso foi emitida
        output = out.getvalue()
        self.assertIn('Department " Administração" already exists.', output)
    
    def test_no_user_found(self):
        # Deleta o usuário de ID 1
        get_user_model().objects.filter(id=1).delete()

        # Captura a saída do comando
        out = StringIO()
        with self.assertRaises(get_user_model().DoesNotExist):
            call_command('populate', stdout=out)


User = get_user_model()

@pytest.mark.django_db
def test_create_superuser():
    """Test create super user"""
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="admin123"
        )
    assert User.objects.filter(username="admin").exists()
