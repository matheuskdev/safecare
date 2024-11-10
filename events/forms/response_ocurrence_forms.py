from django import forms

from events.models import ResponseOcurrence


class ResponseOcurrenceForm(forms.ModelForm):
    class Meta:
        model = ResponseOcurrence
        fields = [
            'ocurrence',
            'meta',
            'description',
            'send_manager',
            'event_investigation',
            'incident_classification',
            'ocurrence_classification',
            'damage_classification',
        ]
        widgets = {
            'meta': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descrição da Trataiva',
                    'required': True,
                }
            ),
            'send_manager': forms.RadioSelect(
                choices=[(True, 'Sim'), (False, 'Não')]
            ),
            'event_investigation': forms.RadioSelect(
                choices=[(True, 'Sim'), (False, 'Não')]
            ),
            'incident_classification': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'ocurrence_classification': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'damage_classification': forms.Select(
                attrs={'class': 'form-select'}
            ),
        }
        labels = {
            'ocurrence': 'Ocorrência',
            'meta': 'Meta',
            'description': 'Descrição',
            'send_manager': 'Enviado para o Gestor ?',
            'event_investigation': 'Investigação ?',
            'incident_classification': 'Classificação do Incidente',
            'ocurrence_classification': 'Classificação da Ocorrência',
            'damage_classification': 'Classificação do Dano',
        }
