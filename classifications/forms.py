from django import forms

from .models import (
    IncidentClassification,
    OcurrenceClassification,
    DamageClassification
)


class IncidentClassificationForm(forms.ModelForm):

    class Meta:
        model = IncidentClassification
        fields = [
            'classification'
        ]
        widgets = {
            'classification': forms.Select(
                attrs={'class': 'form-select'}
            )
        }
        labels = {
            'classification': 'Classificação do Incidente'
        }


class OcurrenceClassification(forms.ModelForm):

    class Meta:
        model = OcurrenceClassification
        fields = [
            'classification'
        ]
        widgets = {
            'classification': forms.Select(
                attrs={'class': 'form-select'}
            )
        }
        labels = {
            'classification': 'Classificação da Ocorrência'
        }


class DamageClassification(forms.ModelForm):

    class Meta:
        model = DamageClassification
        fields = [
            'classification'
        ]
        widgets = {
            'classification': forms.Select(
                attrs={'class': 'form-select'}
            )
        }
        labels = {
            'classification': 'Classificação do Dano'
        }
