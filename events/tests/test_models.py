from django.test import TestCase
from django.utils import timezone

from classifications.models import (
    DamageClassification,
    IncidentClassification,
    OcurrenceClassification,
)
from departments.models import Department
from events.models.event_ocurrence_models import EventOcurrence
from events.models.event_patient_models import EventPatient
from utils.test import SetUpInitial


class EventModelsTest(SetUpInitial):
    def setUp(self):
        super().setUp()
        self.reporting_department = Department.objects.get(id=1)
        self.notified_department = Department.objects.get(id=2)
        self.incident_classification = IncidentClassification.objects.create(
            classification="Incidente Grave"
        )
        self.ocurrence_classification = OcurrenceClassification.objects.create(
            classification="Erro Médico"
        )
        self.damage_classification = DamageClassification.objects.create(
            classification="Dano Permanente"
        )

        # Criando um paciente de teste
        self.patient = EventPatient.objects.create(
            patient_name="João da Silva",
            attendance=12345,
            record=67890,
            birth_date="1985-05-15",
            internment_date="2024-01-20",
        )

    def test_event_patient_creation(self):
        # Verifica se o paciente foi criado corretamente
        self.assertEqual(self.patient.patient_name, "João da Silva")
        self.assertEqual(self.patient.attendance, 12345)
        self.assertEqual(self.patient.record, 67890)

    def test_event_ocurrence_creation(self):
        # Criando uma ocorrência associada ao paciente
        event_ocurrence = EventOcurrence.objects.create(
            patient_involved=True,
            ocurrence_date=timezone.now().date(),
            ocurrence_time=timezone.now().time(),
            patient=self.patient,
            reporting_department=self.reporting_department,
            notified_department=self.notified_department,
            incident_classification=self.incident_classification,
            ocurrence_classification=self.ocurrence_classification,
            damage_classification=self.damage_classification,
            description_ocurrence="Descrição da ocorrência",
            immediate_action="Ação imediata realizada",
        )

        # Verificando os campos da ocorrência
        self.assertTrue(event_ocurrence.patient_involved)
        self.assertEqual(
            event_ocurrence.patient.patient_name, "João da Silva"
        )
        self.assertEqual(
            event_ocurrence.reporting_department.name, "Administração"
        )
        self.assertEqual(
            event_ocurrence.notified_department.name, "TI"
        )
        self.assertEqual(
            event_ocurrence.incident_classification.classification, "Incidente Grave"
        )
        self.assertEqual(
            event_ocurrence.ocurrence_classification.classification, "Erro Médico"
        )
        self.assertEqual(
            event_ocurrence.damage_classification.classification, "Dano Permanente"
        )
        self.assertEqual(
            event_ocurrence.description_ocurrence, "Descrição da ocorrência"
        )
        self.assertEqual(
            event_ocurrence.immediate_action, "Ação imediata realizada"
        )
