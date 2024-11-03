"""Module models for events
"""
from django.db import models

from departments.models import Department
from utils import mixins


class EventOcurrence(  # type: ignore[misc]
    mixins.TimestampModelMixin, mixins.SoftDeleteModelMixin
):
    """
    Model representing a Event Ocurrence.
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

    class Meta:  # pylint: disable=too-few-public-methods
        """Class Meta for Event Ocurrence"""

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
        return f"""
        O setor: {self.reporting_department} 
        notificou o setor: {self.notified_department}
    """
