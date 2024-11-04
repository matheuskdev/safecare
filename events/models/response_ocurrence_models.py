"""Models for response in ocurrences"""
from datetime import timedelta

from django.db import models
from django.utils import timezone

from classifications.models import (
    DamageClassification,
    IncidentClassification,
    OcurrenceClassification,
)
from events.models.metas_models import Metas
from events.models.ocurrence_description_models import OcurrenceDescription
from utils import mixins


class ResponseOcurrence(
    mixins.TimestampModelMixin, mixins.OwnerModelMixin
):
    ocurrence = models.OneToOneField(
        'EventOcurrence',
        on_delete=models.PROTECT,
        help_text='Ocorrencia relacionada',
        related_name='response_ocurrence',
    )
    ocurrence_description = models.ForeignKey(
        OcurrenceDescription,
        on_delete=models.PROTECT,
        help_text='Descrição da Ocorrência'
    )
    meta = models.OneToOneField(
        Metas,
        on_delete=models.PROTECT,
        help_text='Meta',
        related_name='meta_response_ocurrence'
    )
    description = models.TextField(
        help_text='Descrição da tratativa'
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

    class Meta:  # pylint: disable=too-few-public-methods
        """Class Meta for Response Ocurrence"""

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
        return f"""
            {self.owner.username}
            realizou a tratativa da ocorrência {self.ocurrence}
        """

    def calculate_deadline(self):
        """
        Calcula o prazo de retorno com base nas classificações de ocorrência e dano.
        O prazo é definido somando-se um número de dias com base nas classificações.
        """

        days_of_response = 0

        # Classificação da ocorrência
        if self.ocurrence_classification.classification == "Improcedente":
            days_of_response += 1
        elif self.ocurrence_classification.classification in [
            "Não conformidade", "Circustância de Risco", 
            "Quebra de contratualização", "Desvio da Qualidade"
        ]:
            days_of_response += 15
        elif self.ocurrence_classification.classification == "Incidente sem dano":
            days_of_response += 10

        # Classificação do dano
        if self.damage_classification.classification == "Nenhum":
            days_of_response += 15
        elif self.damage_classification.classification == "Dano Leve":
            days_of_response += 7
        elif self.damage_classification.classification == "Dano Moderado":
            days_of_response += 5
        elif self.damage_classification.classification == "Dano Grave":
            days_of_response += 3
        elif self.damage_classification.classification == "Dano Óbito":
            days_of_response += 15

        return days_of_response

    def save(self, *args, **kwargs):
        """
        Sobrescreve o método save para calcular o prazo automaticamente
        se não houver um valor de 'deadline_response' definido.
        """
        if not self.deadline_response:
            days_of_response = self.calculate_deadline()
            if days_of_response > 0:
                self.deadline_response = timezone.now().date() + timedelta(days=days_of_response)
        super().save(*args, **kwargs)
