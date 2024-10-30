from django.core.exceptions import ValidationError
from django.db import models

from utils import mixins, validators


class Department(
    mixins.TimestampModelMixin,
    mixins.OwnerModelMixin,
    mixins.SoftDeleteModelMixin,
):
    """
    Model representing a Department
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
        if not self.name or not self.name.strip():
            raise ValidationError("O campo 'name' não pode estar vazio.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
