"""Module models for events."""

from django.db import models
from departments.models import Department
from utils import mixins


class EventOcurrence(  # type: ignore[misc]
    mixins.TimestampModelMixin, mixins.SoftDeleteModelMixin
):
    """
    Model representing an Event Occurrence.

    This model captures the details of an event occurrence, including whether 
    a patient was involved, the date and time of the occurrence, the departments 
    involved, and a description of the immediate action taken.

    Inherits from:
        mixins.TimestampModelMixin: Adds `created_at` and `updated_at` timestamp fields.
        mixins.SoftDeleteModelMixin: Adds soft delete functionality with an `is_deleted` flag.

    Attributes:
        patient_involved (BooleanField): Indicates if a patient was involved in the event.
        ocurrence_date (DateField): The date when the event occurred.
        ocurrence_time (TimeField): The time when the event occurred.
        patient (ForeignKey): A reference to the patient involved in the event, if any.
        reporting_department (ForeignKey): The department reporting the event.
        notified_department (ForeignKey): The department being notified about the event.
        description_ocurrence (TextField): A detailed description of the event.
        immediate_action (TextField): Immediate actions taken following the event.
    
    Meta:
        ordering (list): Default ordering by `created_at`.
        verbose_name (str): Human-readable name for the model.
        verbose_name_plural (str): Plural form of the human-readable name.
        indexes (list): Database indexes for optimizing queries on specific fields.
    
    Methods:
        __str__(): Returns a string representation of the event occurrence, 
                   detailing the departments involved.
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
        help_text='O que foi realizado após a ocorrência / Ação imediata'
    )

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta options for EventOcurrence model."""
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
        Return a string representation of the event occurrence.

        The representation includes the reporting department and the 
        notified department for better clarity.

        Returns:
            str: A formatted string showing which department reported 
                 the event and which department was notified.
        """
        return f"""
        O setor: {self.reporting_department} 
        notificou o setor: {self.notified_department}
        """
