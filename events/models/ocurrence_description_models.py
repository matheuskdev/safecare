"""Models for Metas Anvisa"""
from django.db import models

from utils import mixins


class OcurrenceDescription(
    mixins.TimestampModelMixin,
    mixins.OwnerModelMixin
):
    """
    Model representing the description of an occurrence.

    This model is used to store descriptions of occurrences, which are
    related to specific events or actions within the system. It includes 
    the name of the occurrence description and inherits functionality 
    from mixins for timestamps and ownership.

    Inherits from:
        TimestampModelMixin: Provides fields for created_at and updated_at timestamps.
        OwnerModelMixin: Provides ownership-related fields, such as the owner of the occurrence.

    Attributes:
        name (TextField): The name or description of the occurrence, limited to 255 characters.

    Meta:
        ordering (list): Default ordering of occurrence descriptions by creation timestamp (created_at).
        verbose_name (str): Human-readable name for the model.
        verbose_name_plural (str): Plural form of the human-readable name.
        indexes (list): Database index on the `name` field to improve query performance.

    Methods:
        __str__():
            Returns the name of the occurrence description as a string.
    """
    
    name = models.TextField(
        max_length=255,
        help_text='Descrição da Ocorrência'
    )

    class Meta:
        """Meta options for OcurrenceDescription model"""
        ordering = ['created_at']
        verbose_name = 'Descrição da Ocorrência'
        verbose_name_plural = 'Descrições das Ocorrências'
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self) -> str:
        """
        Return a string representation of the occurrence description.

        This method returns the name of the occurrence description, which 
        is useful for displaying the description in textual formats 
        (e.g., admin interfaces).

        Returns:
            str: The name of the occurrence description.
        """
        return f"{self.name}"
