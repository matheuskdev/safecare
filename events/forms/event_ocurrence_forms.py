from django import forms

from events.models import EventOcurrence


class EventOcurrenceForm(forms.ModelForm):
    class Meta:
        model = EventOcurrence
        fields = [
            'patient_involved',
            'ocurrence_date',
            'ocurrence_time',
            'reporting_department',
            'notified_department',
            'description_ocurrence',
            'immediate_action',
        ]
        widgets = {
            'patient_involved': forms.RadioSelect(
                choices=[(True, 'Sim'), (False, 'Não')]
            ),
            'ocurrence_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'required': True,
                },
                format='%Y-%m-%d',
            ),
            'ocurrence_time': forms.TimeInput(
                attrs={'class': 'form-control', 'type': 'time'}
            ),
            'reporting_department': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'notified_department': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'description_ocurrence': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descrição da Ocorrência',
                    'required': True,
                }
            ),
            'immediate_action': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'O que foi realizado após a ocorrência / Ação imediata',
                    'required': True,
                }
            ),
        }
        labels = {
            'patient_involved': 'Paciente envolvido ?',
            'ocurrence_date': 'Data da Ocorrência',
            'ocurrence_time': 'Hora da Ocorrência',
            'reporting_department': 'Setor Notificante',
            'notified_department': 'Setor Notificado',
            'description_ocurrence': 'Descrição da Ocorrência',
            'immediate_action': 'Ação Imediata',
        }
