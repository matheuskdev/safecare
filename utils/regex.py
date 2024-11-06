from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r"^\d{9,15}$",
    message="Número de telefone deve conter entre 9 e 15 dígitos.",
)
"""
A RegexValidator instance used to validate phone numbers.

This validator ensures that a phone number contains only digits 
and is between 9 and 15 characters in length. It is intended for 
use with fields that capture phone numbers in models or forms.

Attributes:
    regex (str): The regular expression pattern used to validate the input.
    message (str): The error message displayed when the input does not match 
                   the specified pattern.
"""
