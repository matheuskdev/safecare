"""Models for Metas Anvisa"""
from django.db import models

from utils import mixins


class OcurrenceDescription(
    mixins.TimestampModelMixin,
    mixins.OwnerModelMixin
):
    name = models.TextField(
        max_length=255,
        help_text='Descrição da Ocorrência'
    )

    class Meta:
        """Class Meta for Ocurrence Description"""

        ordering = ['created_at']
        verbose_name = 'Descrição da Ocorrência'
        verbose_name_plural = 'Descrições das Ocorrências'
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self) -> str:
        return f"{self.name}"
