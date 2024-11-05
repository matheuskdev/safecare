from utils.test import SetUpInitial
from django.db.utils import IntegrityError
from events.models.gender_models import Gender


class GenderModelTest(SetUpInitial):
    def setUp(self):
        super().setUp()
        # Criar um objeto Gender para ser usado nos testes
        self.gender = Gender.objects.create(
            name="Masculino"
        )

    def test_create_gender(self):
        """Testa se o objeto Gender é criado corretamente."""
        self.assertEqual(self.gender.name, "Masculino")

    def test_create_null(self):
        """Testa se a criação de um objeto Gender com 'name=None' levanta uma IntegrityError."""
        with self.assertRaises(IntegrityError):
            Gender.objects.create(name=None)  # O campo 'name' não pode ser nulo

    def test_gender_str(self):
        """Testa o método __str__ do modelo Gender."""
        self.assertEqual(str(self.gender), "Masculino")

    def test_gender_ordering(self):
        """Testa se o modelo é ordenado corretamente pelo campo 'name'."""
        gender1 = Gender.objects.create(name="Femenino")
        gender2 = Gender.objects.create(name="Outros(as)")
        genders = Gender.objects.all()
        self.assertEqual(list(genders), [gender1, gender2, self.gender])  # Ordenado por 'name'
