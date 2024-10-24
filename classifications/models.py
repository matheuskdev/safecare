from django.db import models

from utils import mixins


class IncidentClassification(  # type: ignore[misc]
    mixins.TimestampModelMixin,
    mixins.SoftDeleteModelMixin
):
    """
    Model representing a Incident Classification.
    """
    classification = models.CharField(
        max_length=255,
        help_text="Tipo da classificação do incidente."
    )

    class Meta:
        ordering = ["classification"]
        verbose_name = "Classificação de Incidente"
        verbose_name_plural = "Classificações dos Incidentes"
        indexes = [
            models.Index(fields=["classification"]), 
        ]

    def __str__(self) -> str:
        return self.classification


class OcurrenceClassification(  # type: ignore[misc]
    mixins.TimestampModelMixin,
    mixins.SoftDeleteModelMixin
):
    """
    Model representing a Ocurrence Classification.
    """
    classification = models.CharField(
        max_length=255,
        help_text="Tipo da classificação da ocorrência."
    )

    class Meta:
        ordering = ["classification"]
        verbose_name = "Classificação de Ocorrência"
        verbose_name_plural = "Classificações das Ocorrências"
        indexes = [
            models.Index(fields=["classification"]), 
        ]

    def __str__(self) -> str:
        return self.classification


class DamageClassification(  # type: ignore[misc]
    mixins.TimestampModelMixin,
    mixins.SoftDeleteModelMixin
):
    """
    Model representing a Damage Classification.
    """
    classification = models.CharField(
        max_length=255,
        help_text="Tipo da classificação do dano."
    )

    class Meta:
        ordering = ["classification"]
        verbose_name = "Classificação de Dano"
        verbose_name_plural = "Classificações dos Danos"
        indexes = [
            models.Index(fields=["classification"]), 
        ]

    def __str__(self) -> str:
        return self.classification
