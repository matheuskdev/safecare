from django.core.validators import MinLengthValidator
from django.db import models

from classifications.models import (
    DamageClassification,
    IncidentClassification,
    OcurrenceClassification,
)
from departments.models import Department
from utils import mixins


class EventPatient(# type: ignore[misc]
    mixins.TimestampModelMixin,
    mixins.SoftDeleteModelMixin
):
    """
    Model representing a Event Patient
    """
    patient_name = models.CharField(
        max_length=225,
        help_text='Nome do paciente'
    )
    attendance = models.IntegerField(
        help_text='Número do Atendimento',
    )
    record = models.IntegerField(
        help_text='Número do prontuário.',
    )
    birth_date = models.DateField(
        help_text='Data de nascimento.'
    )
    internment_date = models.DateField(
        help_text='Data de internação.'
    )

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Paciente Ocorrência"
        verbose_name_plural = "Pacientes Ocorrências"
        indexes = [
            models.Index(fields=["patient_name"]),
            models.Index(fields=["attendance"]),
            models.Index(fields=["record"]),
            models.Index(fields=["birth_date"]),
            models.Index(fields=["internment_date"]), 
        ]

    def __str__(self) -> str:
        return f'Paciente: {self.patient_name}, Atendimento: {self.attendance}'


class EventOcurrence(# type: ignore[misc]
    mixins.TimestampModelMixin,
    mixins.SoftDeleteModelMixin
):
    """
    Model representing a Event Ocurrence.
    """

    patient_involved = models.BooleanField(
        default=False,
        help_text="A ocorrência envolveu algum paciente ?"
    )
    ocurrence_date = models.DateField(
        help_text="Data da ocorrência"
    )
    ocurrence_time = models.TimeField(
        help_text="Hora da ocorrência"
    )
    patient = models.ForeignKey(
        'EventPatient',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Paciente envolvido na ocorrência",
        related_name='patient_events'
    )
    reporting_department = models.ForeignKey(
        Department,
        on_delete=models.DO_NOTHING,
        help_text="Setor que está reportando",
        related_name='reporting_events'
    )
    notified_department = models.ForeignKey(
        Department,
        on_delete=models.DO_NOTHING,
        help_text="Setor que está sendo notificado",
        related_name='notified_events'
    )
    incident_classification = models.ForeignKey(
        IncidentClassification,
        on_delete=models.DO_NOTHING,
        help_text="Classificação do Incidente",
        related_name='incident_events'
    )
    ocurrence_classification = models.ForeignKey(
        OcurrenceClassification,
        on_delete=models.DO_NOTHING,
        help_text="Classificação da Ocorrência",
        related_name='ocurrence_events'
    )
    damage_classification = models.ForeignKey(
        DamageClassification,
        on_delete=models.DO_NOTHING,
        help_text="Classificação do Dano",
        related_name='damage_events'
    )
    description_ocurrence = models.TextField(
        help_text="Descrição da ocorrência"
    )
    immediate_action = models.TextField(
        help_text="O que foi realizado após a corrência / Ação imediata"
    )
    

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"
        indexes = [
            models.Index(fields=["patient_involved"]),
            models.Index(fields=["ocurrence_date"]),
            models.Index(fields=["reporting_department"]),
            models.Index(fields=["notified_department"]),
            models.Index(fields=["incident_classification"]),
            models.Index(fields=["ocurrence_classification"]),
            models.Index(fields=["damage_classification"]),  
        ]

    def __str__(self) -> str:
        return f'O setor: {self.reporting_department} notificou o setor: {self.notified_department}'
