from django.db import models

from utils import mixins


class IncidentClassification(  # type: ignore[misc]
    mixins.TimestampModelMixin, mixins.SoftDeleteModelMixin
):
    """
    Model representing an Incident Classification.

    This model stores information about the classification of incidents,
    including the type of classification and associated metadata for ordering
    and indexing.

    Inherits from:
        TimestampModelMixin: Adds created_at and updated_at timestamps.
        SoftDeleteModelMixin: Allows for soft deletion of the classification.

    Attributes:
        classification (CharField): The type of classification for the incident,
                                     limited to 255 characters.

    Meta:
        ordering (list): The default ordering of classifications by the classification field.
        verbose_name (str): A human-readable singular name for the model.
        verbose_name_plural (str): A human-readable plural name for the model.
        indexes (list): Database index on the `classification` field to optimize queries.

    Methods:
        __str__():
            Returns the classification type as a string.
    """

    classification = models.CharField(
        max_length=255, help_text="Tipo da classificação do incidente."
    )

    class Meta:
        """Meta options for IncidentClassification model."""

        ordering = ["classification"]
        verbose_name = "Classificação de Incidente"
        verbose_name_plural = "Classificações dos Incidentes"
        indexes = [
            models.Index(fields=["classification"]),
        ]

    def __str__(self) -> str:
        """
        Return the classification type as a string.

        This method provides a string representation of the incident classification,
        which can be used for display in admin interfaces and other textual outputs.

        Returns:
            str: The classification type.
        """
        return self.classification


class OcurrenceClassification(  # type: ignore[misc]
    mixins.TimestampModelMixin, mixins.SoftDeleteModelMixin
):
    """
    Model representing an Ocurrence Classification.

    This model stores information about the classification of occurrences,
    including the type of classification and associated metadata for ordering
    and indexing.

    Inherits from:
        TimestampModelMixin: Adds created_at and updated_at timestamps.
        SoftDeleteModelMixin: Allows for soft deletion of the classification.

    Attributes:
        classification (CharField): The type of classification for the occurrence,
                                     limited to 255 characters.

    Meta:
        ordering (list): The default ordering of classifications by the classification field.
        verbose_name (str): A human-readable singular name for the model.
        verbose_name_plural (str): A human-readable plural name for the model.
        indexes (list): Database index on the `classification` field to optimize queries.

    Methods:
        __str__():
            Returns the classification type as a string.
    """

    classification = models.CharField(
        max_length=255, help_text="Tipo da classificação da ocorrência."
    )

    class Meta:
        """Meta options for OcurrenceClassification model."""

        ordering = ["classification"]
        verbose_name = "Classificação de Ocorrência"
        verbose_name_plural = "Classificações das Ocorrências"
        indexes = [
            models.Index(fields=["classification"]),
        ]

    def __str__(self) -> str:
        """
        Return the classification type as a string.

        This method provides a string representation of the occurrence classification,
        which can be used for display in admin interfaces and other textual outputs.

        Returns:
            str: The classification type.
        """
        return self.classification


class DamageClassification(  # type: ignore[misc]
    mixins.TimestampModelMixin, mixins.SoftDeleteModelMixin
):
    """
    Model representing a Damage Classification.

    This model stores information about the classification of damage, including
    the type of classification and associated metadata for ordering and indexing.

    Inherits from:
        TimestampModelMixin: Adds created_at and updated_at timestamps.
        SoftDeleteModelMixin: Allows for soft deletion of the classification.

    Attributes:
        classification (CharField): The type of classification for the damage,
                                     limited to 255 characters.

    Meta:
        ordering (list): The default ordering of classifications by the classification field.
        verbose_name (str): A human-readable singular name for the model.
        verbose_name_plural (str): A human-readable plural name for the model.
        indexes (list): Database index on the `classification` field to optimize queries.

    Methods:
        __str__():
            Returns the classification type as a string.
    """

    classification = models.CharField(
        max_length=255, help_text="Tipo da classificação do dano."
    )

    class Meta:
        """Meta options for DamageClassification model."""

        ordering = ["classification"]
        verbose_name = "Classificação de Dano"
        verbose_name_plural = "Classificações dos Danos"
        indexes = [
            models.Index(fields=["classification"]),
        ]

    def __str__(self) -> str:
        """
        Return the classification type as a string.

        This method provides a string representation of the damage classification,
        which can be used for display in admin interfaces and other textual outputs.

        Returns:
            str: The classification type.
        """
        return self.classification
