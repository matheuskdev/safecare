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
from responses.models.metas_models import Metas
from responses.models.ocurrence_description_models import OcurrenceDescription
from responses.services.response_ocurrence_services import CalculateDeadline
from utils import mixins


class ResponseOcurrence(mixins.TimestampModelMixin, mixins.OwnerModelMixin):
    """
    Model representing a response to an occurrence in an event management system.

    This model stores information related to the response of a specific occurrence, 
    including its classifications, description, and whether it has been resolved, 
    investigated, or sent to a manager.

    Inherits from:
        TimestampModelMixin: Provides timestamp fields for creation and modification.
        OwnerModelMixin: Provides ownership tracking for the instance.

    Attributes:
        ocurrence (EventOcurrence): The related occurrence.
        ocurrence_description (OcurrenceDescription): Detailed description of the occurrence.
        meta (Metas): Meta information related to the response, based on Anvisa standards.
        description (str): Description of the treatment or actions taken for the occurrence.
        deadline_response (datetime.date): Deadline for responding to the occurrence.
        resolved (bool): Indicates if the occurrence has been resolved.
        send_manager (bool): Indicates if the response has been sent to a manager.
        event_investigation (bool): Indicates if an investigation is ongoing for the event.
        incident_classification (IncidentClassification): Classification of the incident.
        ocurrence_classification (OcurrenceClassification): Classification of the occurrence.
        damage_classification (DamageClassification): Classification of any damage caused.
    """

    ocurrence = models.OneToOneField(
        EventOcurrence,
        on_delete=models.PROTECT,
        help_text="Informe a Ocorrência relacionada",
        related_name="response_ocurrence",
    )
    ocurrence_description = models.ForeignKey(
        OcurrenceDescription,
        on_delete=models.PROTECT,
        help_text="Selecione a descrição da ocorrência",
    )
    meta = models.ForeignKey(
        Metas,
        on_delete=models.PROTECT,
        help_text="Meta Anvisa",
        related_name="meta_response_ocurrence",
    )
    description = models.TextField(
        help_text="Realize a descrição da tratativa"
    )
    deadline_response = models.DateField(
        blank=True, null=True, help_text="Prazo da Resposta"
    )
    resolved = models.BooleanField(default=False, help_text="Resolvido ?")
    send_manager = models.BooleanField(
        default=False, help_text="Enviado para o gestor ?"
    )
    event_investigation = models.BooleanField(
        default=False, help_text="Investigação do Evento ?"
    )
    incident_classification = models.ForeignKey(
        IncidentClassification,
        on_delete=models.DO_NOTHING,
        help_text="Classificação do Incidente",
        related_name="incident_response_ocurrence",
    )
    ocurrence_classification = models.ForeignKey(
        OcurrenceClassification,
        on_delete=models.DO_NOTHING,
        help_text="Classificação da Ocorrência",
        related_name="ocurrence_response_ocurrence",
    )
    damage_classification = models.ForeignKey(
        DamageClassification,
        on_delete=models.DO_NOTHING,
        help_text="Classificação do Dano",
        related_name="damage_response_ocurrence",
    )

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta options for ResponseOcurrence model"""

        ordering = ["created_at"]
        verbose_name = "Tratativa"
        verbose_name_plural = "Tratativas"
        indexes = [
            models.Index(fields=["ocurrence"]),
            models.Index(fields=["send_manager"]),
            models.Index(fields=["event_investigation"]),
            models.Index(fields=["incident_classification"]),
            models.Index(fields=["ocurrence_classification"]),
            models.Index(fields=["damage_classification"]),
        ]

    def __str__(self) -> str:
        """
        Return a string representation of the response occurrence.

        The string representation includes the owner's username and the
        related occurrence to facilitate display in interfaces.

        Returns:
            str: A string representing the owner and the treated occurrence.
        """

        return f"{self.owner.username} realizou a tratativa da ocorrência {self.ocurrence}"


def save(self, *args: dict[Any], **kwargs: dict[Any]) -> None:
    """
    Override the save method to automatically calculate the response deadline.

    This method checks if the 'deadline_response' field is unset. If it is,
    it calculates the deadline based on predefined rules from `CalculateDeadline`
    and assigns the result to 'deadline_response' before saving the model instance.

    Args:
        *args (dict[Any]): Positional arguments passed to the parent save method.
        **kwargs (dict[Any]): Keyword arguments passed to the parent save method.
    """
    calculate_deadline: CalculateDeadline = CalculateDeadline(
        ocurrence=self.ocurrence_classification,
        damage=self.damage_classification,
    )

    # Calculate the response deadline based on classifications
    days_of_response = calculate_deadline.calculate()

    if not self.deadline_response and days_of_response > 0:
        self.deadline_response = timezone.now().date() + timedelta(
            days=days_of_response
        )

    super().save(*args, **kwargs)
