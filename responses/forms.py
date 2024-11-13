from django import forms

from responses.models import ResponseOcurrence


class ResponseOcurrenceForm(forms.ModelForm):
    """
    Form for creating and updating ResponseOcurrence instances.

    This form is used to handle user input for creating or editing 
    `ResponseOcurrence` objects. It customizes the appearance and behavior 
    of the fields with specific widgets and labels for a better user experience.

    Inherits from:
        forms.ModelForm: Django's base class for model-based forms.

    Attributes:
        Meta (class): Contains metadata options for the form fields.
    """

    class Meta:
        model = ResponseOcurrence
        fields = [
            "meta",
            "description",
            "send_manager",
            "event_investigation",
            "incident_classification",
            "ocurrence_classification",
            "damage_classification",
        ]
        widgets = {
            "meta": forms.Select(attrs={"class": "form-select"}),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Descrição da Tratativa",
                    "required": True,
                }
            ),
            "send_manager": forms.RadioSelect(
                choices=[(True, "Sim"), (False, "Não")]
            ),
            "event_investigation": forms.RadioSelect(
                choices=[(True, "Sim"), (False, "Não")]
            ),
            "incident_classification": forms.Select(
                attrs={"class": "form-select"}
            ),
            "ocurrence_classification": forms.Select(
                attrs={"class": "form-select"}
            ),
            "damage_classification": forms.Select(
                attrs={"class": "form-select"}
            ),
        }
        labels = {
            "ocurrence": "Ocorrência",
            "meta": "Meta",
            "description": "Descrição",
            "send_manager": "Enviado para o Gestor?",
            "event_investigation": "Investigação?",
            "incident_classification": "Classificação do Incidente",
            "ocurrence_classification": "Classificação da Ocorrência",
            "damage_classification": "Classificação do Dano",
        }
