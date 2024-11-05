"""Models for genere."""
from django.db import models


class Genere(models.Model):
    """Class for genere"""
    name = models.TextField(
        max_length=255,
        help_text='Gênero'
    )

    class Meta:  # pylint: disable=too-few-public-methods
        """Class Meta for genere."""

        ordering = ['name']
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self) -> str:
        return f'{self.name}'
