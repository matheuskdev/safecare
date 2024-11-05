from django.db.utils import IntegrityError

from events.models.metas_models import Metas
from utils.test import SetUpInitial


class MetasModelTest(SetUpInitial):
    def setUp(self):
        super().setUp()
        self.meta = Metas.objects.create(
            name="Meta de Segurança Sanitária",
            owner_id=self.user.id
        )

    def test_create_meta(self):
        """Testa se o objeto Metas é criado corretamente."""
        self.assertEqual(self.meta.name, "Meta de Segurança Sanitária")
        self.assertIsNotNone(self.meta.created_at)  # Verifica se o campo created_at é preenchido

    def test_create_null(self):
        """Testa a criação de um objeto Metas com o campo 'name' em branco."""
        with self.assertRaises(IntegrityError):
            Metas.objects.create(name=None, owner_id=self.user.id)

    def test_meta_str(self):
        """Testa o método __str__ do modelo Metas."""
        self.assertEqual(str(self.meta), "Meta de Segurança Sanitária")

    def test_meta_ordering(self):
        """Testa se o modelo é ordenado corretamente pelo campo 'created_at'."""
        meta1 = Metas.objects.create(
            name="Primeira Meta",
            owner_id=self.user.id
        )
        meta2 = Metas.objects.create(
            name="Segunda Meta",
            owner_id=self.user.id
        )
        metas = Metas.objects.all()
        self.assertEqual(list(metas), [self.meta, meta1, meta2])
