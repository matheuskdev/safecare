"""Modulo for model race"""
from django.db import models


class Race(models.Model):
    """Class for race."""
    name = models.TextField(
        max_length=255,
        help_text='Raça'
    )

    class Meta:  # pylint: disable=too-few-public-methods
        """Class Meta for race."""

        ordering = ['name']
        verbose_name = 'Raça'
        verbose_name_plural = 'Raças'
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self) -> str:
        return f'{self.name}'
