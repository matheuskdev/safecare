from django import forms

from manager_responses.models import ManagerResponse


class ManagerResponseForm(forms.ModelForm):
    """
    Form for creating and updating ManagerResponse instances.

    This form is used to handle user input for creating or editing
    `ManagerResponse` objects. It customizes the appearance and behavior
    of the fields with specific widgets and labels for a better user experience.

    Inherits from:
        forms.ModelForm: Django's base class for model-based forms.

    Attributes:
        Meta (class): Contains metadata options for the form fields.
    """  # noqa: #501

    class Meta:
        model = ManagerResponse
        fields: list[str] = [
            "response_text",
        ]
        widgets: dict[str, forms.Textarea] = {
            "response_text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Descrição da Tratativa",
                    "required": True,
                }
            ),
        }
        labels: dict[str, str] = {
            "response_text": "Ocorrência",
        }
