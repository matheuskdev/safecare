from django import forms

from .models import EventOcurrence, EventPatient


class EventPatientForm(forms.ModelForm):
    """Class for Event Patient Form"""
    class Meta:  
        """A class meta"""
        model = EventPatient
        fields = [
            'patient_name',
            'attendance',
            'record',
            'birth_date',
            'internment_date',
        ]
        widgets = {
            'patient_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome do Paciente',
                    'required': True,
                    'pattern': '^[A-Za-zÀ-ú\s]+$',
                    'title': 'Somente letras e espaços são permitidos',
                }
            ),
            'attendance': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Atendimento',
                    'required': True,
                }
            ),
            'record': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Número do Prontuário'
                }
            ),
            'birth_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'placeholder': 'Data de Nascimento',
                    'required': True,
                },
                format='%Y-%m-%d',
            ),
            'internment_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'placeholder': 'Data do Internamento',
                    'required': True,
                },
                format='%Y-%m-%d',
            ),
        }
        labels = {
            'patient_name': 'Nome do Paciente',
            'attendance': 'Atendimento',
            'record': 'Prontuário',
            'birth_date': 'Data de Nascimento',
            'internment_date': 'Data da Internação',
        }


class EventOcurrenceForm(forms.ModelForm):
    class Meta:
        model = EventOcurrence
        fields = [
            'patient_involved',
            'ocurrence_date',
            'ocurrence_time',
            'reporting_department',
            'notified_department',
            'incident_classification',
            'ocurrence_classification',
            'damage_classification',
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
            'incident_classification': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'ocurrence_classification': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'damage_classification': forms.Select(
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
            'incident_classification': 'Classificação do Incidente',
            'ocurrence_classification': 'Classificação da Ocorrência',
            'damage_classification': 'Classificação do Dano',
            'description_ocurrence': 'Descrição da Ocorrência',
            'immediate_action': 'Ação Imediata',
        }
