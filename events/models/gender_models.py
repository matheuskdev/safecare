"""Models for gender."""

from django.db import models


class Gender(models.Model):
    """
    Model representing gender.

    This model defines a gender entity, storing the name of the gender
    with a text field and providing metadata for database indexing
    and ordering.

    Attributes:
        name (TextField): The name of the gender, limited to 255 characters.

    Meta:
        ordering (list): Default ordering of gender objects by name.
        verbose_name (str): Human-readable name for the model.
        verbose_name_plural (str): Plural form of the human-readable name.
        indexes (list): Database index on the `name` field to optimize query performance.

    Methods:
        __str__(): Returns the name of the gender as a string.
    """

    name = models.TextField(max_length=255, help_text="Gênero")

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta options for Gender model."""

        ordering = ["name"]
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self) -> str:
        """
        Return a string representation of the gender.

        This method returns the name of the gender, making it easy
        to display gender names in the admin interface and other
        textual representations.

        Returns:
            str: The name of the gender.
        """
        return f"{self.name}"
