"""Module models for events
"""
from django.db import models

from departments.models import Department
from utils import mixins


class EventOcurrence(  # type: ignore[misc]
    mixins.TimestampModelMixin, mixins.SoftDeleteModelMixin
):
    """
    Represents an occurrence related to an event within the system.
    Stores details like date, time, involved departments, and actions taken.

    Inherits from:
        - mixins.TimestampModelMixin: Adds automatic creation and updating of date fields.
        - mixins.SoftDeleteModelMixin: Allows logical deletion of records.

    Args:
        patient_involved (bool): Indicates if a patient was involved in the occurrence.
        ocurrence_date (DateField): The date of the occurrence.
        ocurrence_time (TimeField): The time of the occurrence.
        patient (ForeignKey, Optional): Foreign key to an EventPatient model (optional).
        reporting_department (ForeignKey): Foreign key to the reporting department.
        notified_department (ForeignKey): Foreign key to the notified department.
        description_ocurrence (TextField): Detailed description of the occurrence.
        immediate_action (TextField): Actions taken after the occurrence.
    """

    patient_involved = models.BooleanField(
        default=False, help_text='A ocorrência envolveu algum paciente ?'
    )
    ocurrence_date = models.DateField(help_text='Data da ocorrência')
    ocurrence_time = models.TimeField(help_text='Hora da ocorrência')
    patient = models.ForeignKey(
        'EventPatient',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='Paciente envolvido na ocorrência',
        related_name='patient_events',
    )
    reporting_department = models.ForeignKey(
        Department,
        on_delete=models.DO_NOTHING,
        help_text='Setor que está reportando',
        related_name='reporting_events',
    )
    notified_department = models.ForeignKey(
        Department,
        on_delete=models.DO_NOTHING,
        help_text='Setor que está sendo notificado',
        related_name='notified_events',
    )
    
    description_ocurrence = models.TextField(
        help_text='Descrição da ocorrência'
    )
    immediate_action = models.TextField(
        help_text='O que foi realizado após a corrência / Ação imediata'
    )

    class Meta:
        # pylint: disable=too-few-public-methods, missing-class-docstring
        ordering = ['created_at']
        verbose_name = 'Ocorrência'
        verbose_name_plural = 'Ocorrências'
        indexes = [
            models.Index(fields=['patient_involved']),
            models.Index(fields=['ocurrence_date']),
            models.Index(fields=['reporting_department']),
            models.Index(fields=['notified_department']),
        ]

    def __str__(self) -> str:
        """
        Returns:
            str: Returns a string containing the reporting_department name and notified_department.
        """
        return f"""
        O setor: {self.reporting_department} 
        notificou o setor: {self.notified_department}
    """
