from classifications.models import (
    DamageClassification,
    IncidentClassification,
    OcurrenceClassification,
)
from utils.test import SetUpInitial


class IncidentClassificationModelTest(SetUpInitial):
    def setUp(self):
        # Criar um objeto de IncidentClassification
        self.ic1 = IncidentClassification.objects.create(
            classification="Médio"
        )
        self.ic2 = IncidentClassification.objects.create(classification="Alta")
        self.ic3 = IncidentClassification.objects.create(
            classification="Baixa"
        )

    def test_create_incident_classification(self):
        """Testa se a classificação de incidente é criada corretamente."""
        self.assertEqual(
            self.ic1.classification,
            "Médio",
        )

    def test_incident_classification_str(self):
        """Testa o método __str__ do modelo IncidentClassification."""
        self.assertEqual(str(self.ic1), "Médio")

    def test_incident_classification_ordering(self):
        """Testa se o modelo é ordenado corretamente pelo campo 'classification'."""

        classifications = IncidentClassification.objects.all()
        self.assertEqual(
            list(classifications), [self.ic2, self.ic3, self.ic1]
        )  # Ordenado por nome


class OcurrenceClassificationModelTest(SetUpInitial):
    def setUp(self):
        # Criar um objeto de OcurrenceClassification
        self.oc1 = OcurrenceClassification.objects.create(
            classification="Médio"
        )
        self.oc2 = OcurrenceClassification.objects.create(
            classification="Leve"
        )
        self.oc3 = OcurrenceClassification.objects.create(
            classification="Grave"
        )

    def test_create_ocurrence_classification(self):
        """Testa se a classificação de ocorrência é criada corretamente."""
        self.assertEqual(
            self.oc1.classification,
            "Médio",
        )

    def test_ocurrence_classification_str(self):
        """Testa o método __str__ do modelo OcurrenceClassification."""
        self.assertEqual(str(self.oc1), "Médio")

    def test_ocurrence_classification_ordering(self):
        """Testa se o modelo é ordenado corretamente pelo campo 'classification'."""

        classifications = OcurrenceClassification.objects.all()

        self.assertEqual(list(classifications), [self.oc3, self.oc2, self.oc1])


class DamageClassificationModelTest(SetUpInitial):
    def setUp(self):
        # Criar um objeto de DamageClassification
        self.dc1 = DamageClassification.objects.create(classification="Leve")
        self.dc2 = DamageClassification.objects.create(
            classification="Moderado"
        )
        self.dc3 = DamageClassification.objects.create(classification="Severo")

    def test_create_damage_classification(self):
        """Testa se a classificação de dano é criada corretamente."""
        self.assertEqual(
            self.dc1.classification,
            "Leve",
        )

    def test_damage_classification_str(self):
        """Testa o método __str__ do modelo DamageClassification."""
        self.assertEqual(str(self.dc1), "Leve")

    def test_damage_classification_ordering(self):
        """Testa se o modelo é ordenado corretamente pelo campo 'classification'."""

        classifications = DamageClassification.objects.all()
        self.assertEqual(
            list(classifications), [self.dc1, self.dc2, self.dc3]
        )  # Ordenado por nome
