from django import forms

from .models import (
    DamageClassification,
    IncidentClassification,
    OcurrenceClassification,
)


class IncidentClassificationForm(forms.ModelForm):
    """
    Form for handling the classification of incidents.

    Inherits from:
        forms.ModelForm: A Django form for models.

    Meta:
        model (class): The model associated with this form (IncidentClassification).
        fields (list): List of fields to include in the form ("classification").
        widgets (dict): Custom widgets for form fields.
        labels (dict): Custom labels for form fields.
    """

    class Meta:
        model = IncidentClassification
        fields = ["classification"]
        widgets = {
            "classification": forms.Select(attrs={"class": "form-select"})
        }
        labels = {"classification": "Classificação do Incidente"}


class OcurrenceClassificationForm(forms.ModelForm):
    """
    Form for handling the classification of occurrences.

    Inherits from:
        forms.ModelForm: A Django form for models.

    Meta:
        model (class): The model associated with this form (OcurrenceClassification).
        fields (list): List of fields to include in the form ("classification").
        widgets (dict): Custom widgets for form fields.
        labels (dict): Custom labels for form fields.
    """

    class Meta:
        model = OcurrenceClassification
        fields = ["classification"]
        widgets = {
            "classification": forms.Select(attrs={"class": "form-select"})
        }
        labels = {"classification": "Classificação da Ocorrência"}


class DamageClassificationForm(forms.ModelForm):
    """
    Form for handling the classification of damages.

    Inherits from:
        forms.ModelForm: A Django form for models.

    Meta:
        model (class): The model associated with this form (DamageClassification).
        fields (list): List of fields to include in the form ("classification").
        widgets (dict): Custom widgets for form fields.
        labels (dict): Custom labels for form fields.
    """

    class Meta:
        model = DamageClassification
        fields = ["classification"]
        widgets = {
            "classification": forms.Select(attrs={"class": "form-select"})
        }
        labels = {"classification": "Classificação do Dano"}
