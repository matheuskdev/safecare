from django.db.utils import IntegrityError

from events.models.race_models import (
    Race,  # Substitua 'your_app' pelo nome da sua aplicação
)
from utils.test import SetUpInitial


class RaceModelTest(SetUpInitial):
    def setUp(self):
        super().setUp()
        # Criar um objeto Race para ser usado nos testes
        self.race = Race.objects.create(name="Branca")

    def test_create_race(self):
        """Testa se o objeto Race é criado corretamente."""
        self.assertEqual(self.race.name, "Branca")

    def test_create_null(self):
        """Testa se a criação de um objeto Race com 'name=None' levanta uma IntegrityError."""
        with self.assertRaises(IntegrityError):
            Race.objects.create(name=None)  # O campo 'name' não pode ser nulo

    def test_race_str(self):
        """Testa o método __str__ do modelo Race."""
        self.assertEqual(str(self.race), "Branca")

    def test_race_ordering(self):
        """Testa se o modelo é ordenado corretamente pelo campo 'name'."""
        race1 = Race.objects.create(name="Pardo")
        race2 = Race.objects.create(name="Indigena")
        races = Race.objects.all()
        self.assertEqual(
            list(races),
            [
                self.race,
                race2,
                race1,
            ],
        )  # Ordenado por 'name'
