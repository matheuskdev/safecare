from django import forms

from events.models import EventPatient


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
