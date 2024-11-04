from django.db.utils import IntegrityError

from events.models.ocurrence_description_models import OcurrenceDescription
from utils.test import SetUpInitial


class OcurrenceDescriptionModelTest(SetUpInitial):
    def setUp(self):
        super().setUp()
        self.ocurrence = OcurrenceDescription.objects.create(
            name="Não se aplica",
            owner_id=self.user.id
        )

    def test_create_meta(self):
        """Testa se o objeto OcurrenceDescription é criado corretamente."""
        self.assertEqual(self.ocurrence.name, "Não se aplica")
        self.assertIsNotNone(self.ocurrence.created_at)  # Verifica se o campo created_at é preenchido

    def test_create_null(self):
        """Testa a criação de um objeto OcurrenceDescription com o campo 'name' em branco."""
        with self.assertRaises(IntegrityError):
            OcurrenceDescription.objects.create(name=None, owner_id=self.user.id)

    def test_meta_str(self):
        """Testa o método __str__ do modelo OcurrenceDescription."""
        self.assertEqual(str(self.ocurrence), "Não se aplica")

    def test_meta_ordering(self):
        """Testa se o modelo é ordenado corretamente pelo campo 'created_at'."""
        ocurrence1 = OcurrenceDescription.objects.create(
            name="Falha na assistência",
            owner_id=self.user.id
        )
        ocurrence2 = OcurrenceDescription.objects.create(
            name="Falha do transporte",
            owner_id=self.user.id
        )
        ocurrences = OcurrenceDescription.objects.all()
        self.assertEqual(list(ocurrences), [self.ocurrence, ocurrence1, ocurrence2])
