from django.contrib import admin

from .models import EventOcurrence, EventPatient


@admin.register(EventPatient)
class EventPatientAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'attendance', 'record', 'birth_date', 'internment_date')
    search_fields = ('patient_name', 'attendance', 'record')
    list_filter = ('internment_date', 'birth_date')
    date_hierarchy = 'internment_date'
    ordering = ('patient_name',)


@admin.register(EventOcurrence)
class EventOcurrenceAdmin(admin.ModelAdmin):
    list_display = (
        'ocurrence_date', 'ocurrence_time', 'reporting_department', 
        'notified_department', 'incident_classification', 
        'ocurrence_classification', 'damage_classification', 
        'patient_involved'
    )
    search_fields = ('reporting_department__name', 'notified_department__name')
    list_filter = ('ocurrence_date', 'incident_classification', 'patient_involved')
    date_hierarchy = 'ocurrence_date'
    ordering = ('ocurrence_date',)

    # Exibir campos relacionados ao paciente quando for marcado como envolvido
    def get_readonly_fields(self, request, obj=None):
        if obj and obj.patient_involved:
            return super().get_readonly_fields(request, obj) + ('patient',)
        return super().get_readonly_fields(request, obj)

    # Exibir informações do paciente na listagem, caso tenha um paciente associado
    def patient_name(self, obj):
        return obj.patient.patient_name if obj.patient else "Nenhum Paciente"
    patient_name.short_description = "Paciente Envolvido"
