from django.core.exceptions import ValidationError
from django.db import models

from utils import mixins, validators


class Department(
    mixins.TimestampModelMixin,
    mixins.OwnerModelMixin,
    mixins.SoftDeleteModelMixin,
):
    """
    Model representing a department within the organization.

    This model stores information about a department, including its name, description, 
    and associated constraints. It also includes functionality for tracking timestamps 
    and ownership, as well as soft deletion.

    Inherits from:
        TimestampModelMixin: Provides fields for created_at and updated_at timestamps.
        OwnerModelMixin: Provides fields related to ownership, such as the owner of the department.
        SoftDeleteModelMixin: Adds functionality for soft deletion of the department.

    Attributes:
        name (CharField): The name of the department, which must be unique.
        description (CharField): An optional description of the department.

    Meta:
        ordering (list): The default ordering of departments by name.
        verbose_name (str): A human-readable singular name for the model.
        verbose_name_plural (str): A human-readable plural name for the model.
        indexes (list): A database index on the `name` field to improve query performance.
        constraints (list): A unique constraint ensuring the uniqueness of department names.

    Methods:
        save():
            Custom save method to ensure that the `name` field is not empty or just whitespace before saving.
        __str__():
            Returns a string representation of the department using its name.
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        help_text="Nome do departamento. Deve ser único.",
        validators=[validators.validate_not_empty]
    )
    description = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Descrição do departamento. Opcional.",
    )

    class Meta:
        """Meta options for Department model."""
        ordering = ["name"]
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        indexes = [
            models.Index(fields=["name"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_department_name"
            ),
        ]

    def save(self, *args, **kwargs) -> None:
        """
        Override the save method to ensure the `name` field is not empty or whitespace-only.

        This method raises a `ValidationError` if the `name` field is empty or contains only whitespace.
        After the validation, it calls the parent class's `save` method to store the department in the database.

        Args:
            *args: Additional positional arguments to be passed to the parent save method.
            **kwargs: Additional keyword arguments to be passed to the parent save method.
        """
        if not self.name or not self.name.strip():
            raise ValidationError("O campo 'name' não pode estar vazio.")
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return a string representation of the department.

        This method returns the name of the department, which is used for easy display in the 
        admin interface and other textual representations.

        Returns:
            str: The name of the department.
        """
        return self.name
