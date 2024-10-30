"""Module models for events"""
from django.db import models

from utils import mixins


class EventPatient(  # type: ignore[misc]
    mixins.TimestampModelMixin, mixins.SoftDeleteModelMixin
):
    """
    Model representing a Event Patient
    """

    patient_name = models.CharField(
        max_length=225, help_text='Nome do paciente'
    )
    attendance = models.IntegerField(
        help_text='Número do Atendimento',
    )
    record = models.IntegerField(
        help_text='Número do prontuário.',
    )
    birth_date = models.DateField(help_text='Data de nascimento.')
    internment_date = models.DateField(help_text='Data de internação.')

    class Meta:  # pylint: disable=too-few-public-methods
        """Class Meta for Event Patient"""

        ordering = ['created_at']
        verbose_name = 'Paciente Ocorrência'
        verbose_name_plural = 'Pacientes Ocorrências'
        indexes = [
            models.Index(fields=['patient_name']),
            models.Index(fields=['attendance']),
            models.Index(fields=['record']),
            models.Index(fields=['birth_date']),
            models.Index(fields=['internment_date']),
        ]

    def __str__(self) -> str:
        return f'Paciente: {self.patient_name}, Atendimento: {self.attendance}'
