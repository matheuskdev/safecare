"""Validators for applications."""

from django.core.exceptions import ValidationError


def validate_not_empty(value: str) -> None:
    """
    Custom validation function to check if a value is empty.

    This function ensures that the given value is not empty or composed
    solely of whitespace characters. If the value is empty, a
    ValidationError is raised.

    Args:
        value (str): The value to be validated. It should be a non-empty string.

    Raises:
        ValidationError: If the value is empty or contains only whitespace.
    """
    if not value.strip():
        raise ValidationError(
            "Este campo não pode estar vazio.",
            params={"value": value},
        )
