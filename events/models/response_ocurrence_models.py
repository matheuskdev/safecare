"""Models for response in ocurrences"""
from datetime import timedelta
from typing import Any

from django.db import models
from django.utils import timezone

from classifications.models import (
    DamageClassification,
    IncidentClassification,
    OcurrenceClassification,
)
from events.models.event_ocurrence_models import EventOcurrence
from events.models.metas_models import Metas
from events.models.ocurrence_description_models import OcurrenceDescription
from events.services.response_ocurrence_services import CalculateDeadline
from utils import mixins


class ResponseOcurrence(
    mixins.TimestampModelMixin, mixins.OwnerModelMixin
):

    ocurrence = models.OneToOneField(
        EventOcurrence,
        on_delete=models.PROTECT,
        help_text='Informe a Ocorrência relacionada',
        related_name='response_ocurrence',
    )
    ocurrence_description = models.ForeignKey(
        OcurrenceDescription,
        on_delete=models.PROTECT,
        help_text='Selecione a descrição da ocorrência'
    )
    meta = models.OneToOneField(
        Metas,
        on_delete=models.PROTECT,
        help_text='Meta Anvisa',
        related_name='meta_response_ocurrence'
    )
    description = models.TextField(
        help_text='Realize a descrição da tratativa'
    )
    deadline_response = models.DateField(
        blank=True,
        null=True,
        help_text='Prazo da Resposta'
    )
    resolved = models.BooleanField(
        default=False,
        help_text='Resolvido ?'
    )
    send_manager = models.BooleanField(
        default=False,
        help_text='Enviado para o gestor ?'
    )
    event_investigation = models.BooleanField(
        default=False,
        help_text='Investigação do Evento ?'
    )
    incident_classification = models.ForeignKey(
        IncidentClassification,
        on_delete=models.DO_NOTHING,
        help_text='Classificação do Incidente',
        related_name='incident_response_ocurrence',
    )
    ocurrence_classification = models.ForeignKey(
        OcurrenceClassification,
        on_delete=models.DO_NOTHING,
        help_text='Classificação da Ocorrência',
        related_name='ocurrence_response_ocurrence',
    )
    damage_classification = models.ForeignKey(
        DamageClassification,
        on_delete=models.DO_NOTHING,
        help_text='Classificação do Dano',
        related_name='damage_response_ocurrence',
    )
    
    calculate_deadline = CalculateDeadline(
                ocurrence=ocurrence_classification,
                damage=damage_classification
    )

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta options for ResponseOcurrence model"""
        ordering = ['created_at']
        verbose_name = 'Tratativa'
        verbose_name_plural = 'Tratativas'
        indexes = [
            models.Index(fields=['ocurrence']),
            models.Index(fields=['send_manager']),
            models.Index(fields=['event_investigation']),
            models.Index(fields=['incident_classification']),
            models.Index(fields=['ocurrence_classification']),
            models.Index(fields=['damage_classification']),
        ]

    def __str__(self) -> str:
        """
        Return a string representation of the response occurrence.

        This method returns a string that includes the owner's username and 
        the related occurrence, making it easier to display response occurrences 
        in textual representations such as the admin interface.

        Returns:
            str: A string representation of the response occurrence.
        """
        return f"""
            {self.owner.username}
            realizou a tratativa da ocorrência {self.ocurrence}
        """

    def save(self, *args: dict[Any], **kwargs:dict[Any]):
        """
        Override the save method to calculate the deadline automatically 
        if the 'deadline_response' field is not set.

        This method calculates the response deadline based on predefined 
        business logic and assigns it to the 'deadline_response' field before 
        saving the model instance.

        Args:
            *args: Additional positional arguments to be passed to the parent save method.
            **kwargs: Additional keyword arguments to be passed to the parent save method.
        """
        if not self.deadline_response:
            days_of_response = self.calculate_deadline.calculate()
            if days_of_response > 0:
                self.deadline_response = timezone.now().date() + timedelta(days=days_of_response)
        super().save(*args, **kwargs)
