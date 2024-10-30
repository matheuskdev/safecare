"""Validators for applications"""
from django.core.exceptions import ValidationError


def validate_not_empty(value: str) -> None:
    """Função de validação customizada para verificar se o valor está vazio"""
    if not value.strip():
        raise ValidationError(
            "Este campo não pode estar vazio.",
            params={'value': value},
        )
