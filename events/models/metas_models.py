"""Models for Metas Anvisa"""
from django.db import models

from utils import mixins


class Metas(
    mixins.TimestampModelMixin,
    mixins.OwnerModelMixin
):
    name = models.TextField(
        max_length=255,
        help_text='Nome da Meta'
    )

    class Meta:
        """Class Meta for Meta Anvisa"""

        ordering = ['created_at']
        verbose_name = 'Meta'
        verbose_name_plural = 'Metas'
        indexes = [
            models.Index(fields=['name']),
        ]
    
    def __str__(self) -> str:
        return f"{self.name}"