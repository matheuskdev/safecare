"""Modulo for model race"""
from django.db import models


class Race(models.Model):
    """
    Model representing race.

    This model is used to store race information, defining the name 
    of the race entity within the system. It includes basic attributes 
    like the name of the race and provides metadata for ordering and indexing.

    Inherits from:
        models.Model: The base class for Django models.

    Attributes:
        name (TextField): The name of the race, limited to 255 characters.

    Meta:
        ordering (list): Default ordering of race objects by name.
        verbose_name (str): Human-readable name for the model.
        verbose_name_plural (str): Plural form of the human-readable name.
        indexes (list): Database index on the `name` field to optimize query performance.

    Methods:
        __str__():
            Returns the name of the race as a string.
    """

    name = models.TextField(
        max_length=255,
        help_text='Raça'
    )

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta options for Race model."""
        ordering = ['name']
        verbose_name = 'Raça'
        verbose_name_plural = 'Raças'
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self) -> str:
        """
        Return a string representation of the race.

        This method returns the name of the race, making it easy to 
        display race names in textual representations such as the 
        admin interface or other list views.

        Returns:
            str: The name of the race.
        """
        return f'{self.name}'
