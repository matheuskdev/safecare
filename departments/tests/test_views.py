from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse

from departments.models import Department

User = get_user_model()


class DepartmentViewTest(TestCase):
    def setUp(self):
        # Criar um utilizador com permissões para o teste
        self.user = User.objects.create_user(username="testuser", password="password")
        self.user.user_permissions.add(
            Permission.objects.get(codename="view_department"),
            Permission.objects.get(codename="add_department"),
            Permission.objects.get(codename="change_department"),
            Permission.objects.get(codename="delete_department"),
        )

        # Criar um departamento para os testes
        self.department = Department.objects.create(
            name="Recursos Humanos",
            description="Departamento de gestão de pessoas."
        )

    def test_department_list_view(self):
        """Testa se a página de listagem de departamentos é carregada corretamente."""
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("departments:department_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "department_list.html")
        self.assertContains(response, self.department.name)

    def test_department_create_view(self):
        """Testa a criação de um novo departamento."""
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse("departments:department_create"), {
            "name": "Financeiro",
            "description": "Departamento financeiro."
        })
        self.assertEqual(response.status_code, 302)  # Redireciona após o sucesso
        self.assertTrue(Department.objects.filter(name="Financeiro").exists())

    def test_department_detail_view(self):
        """Testa a exibição dos detalhes de um departamento."""
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("departments:department_detail", kwargs={"pk": self.department.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "department_detail.html")
        self.assertContains(response, self.department.name)

    def test_department_update_view(self):
        """Testa a atualização de um departamento existente."""
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse("departments:department_update", kwargs={"pk": self.department.pk}), {
            "name": "RH Atualizado",
            "description": "Departamento atualizado."
        })
        self.assertEqual(response.status_code, 302)  # Redireciona após o sucesso
        self.department.refresh_from_db()
        self.assertEqual(self.department.name, "RH Atualizado")

    def test_department_delete_view(self):
        """Testa a exclusão (soft delete) de um departamento."""
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse("departments:department_delete", kwargs={"pk": self.department.pk}))
        self.assertEqual(response.status_code, 302)  # Redireciona após o sucesso
        self.department.refresh_from_db()
        self.assertTrue(self.department.deleted)  # Assumindo que soft delete marca como deletado
