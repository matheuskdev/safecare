"""Models for Metas Anvisa"""
from django.db import models

from utils import mixins


class Metas(
    mixins.TimestampModelMixin,
    mixins.OwnerModelMixin
):
    """
    Model representing Metas for Anvisa.

    This model is used to store meta information for regulatory purposes.
    It includes the name of the meta and inherits functionality from mixins 
    for timestamps and ownership management.

    Inherits from:
        TimestampModelMixin: Provides created_at and updated_at timestamps.
        OwnerModelMixin: Provides ownership-related fields (e.g., owner).

    Attributes:
        name (TextField): The name of the meta, limited to 255 characters.

    Meta:
        ordering (list): Default ordering of metas by creation timestamp (created_at).
        verbose_name (str): Human-readable name for the model.
        verbose_name_plural (str): Plural form of the human-readable name.
        indexes (list): Database index on the `name` field to improve query performance.

    Methods:
        __str__():
            Returns the name of the meta as a string.
    """
    
    name = models.TextField(
        max_length=255,
        help_text='Nome da Meta'
    )

    class Meta:
        """Meta options for the Metas model"""
        ordering = ['created_at']
        verbose_name = 'Meta'
        verbose_name_plural = 'Metas'
        indexes = [
            models.Index(fields=['name']),
        ]
    
    def __str__(self) -> str:
        """
        Returns the string representation of the meta.

        This method returns the name of the meta, which is useful 
        for displaying the meta in textual formats (e.g., admin interfaces).

        Returns:
            str: The name of the meta.
        """
        return f"{self.name}"
