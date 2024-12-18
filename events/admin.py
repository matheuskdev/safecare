from django.contrib import admin

from events.models.event_ocurrence_models import EventOcurrence
from events.models.event_patient_models import EventPatient
from events.models.gender_models import Gender
from events.models.metas_models import Metas
from events.models.ocurrence_description_models import OcurrenceDescription
from events.models.race_models import Race
from events.models.response_ocurrence_models import ResponseOcurrence


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('id', 'name',)
    ordering = ('id',)


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('id', 'name',)
    ordering = ('id',)

@admin.register(EventPatient)
class EventPatientAdmin(admin.ModelAdmin):
    list_display = (
        'patient_name', 'attendance', 'record', 'birth_date', 'internment_date'
    )
    search_fields = ('patient_name', 'attendance', 'record')
    list_filter = ('internment_date', 'birth_date')
    date_hierarchy = 'internment_date'
    ordering = ('patient_name',)


@admin.register(EventOcurrence)
class EventOcurrenceAdmin(admin.ModelAdmin):
    list_display = (
        'ocurrence_date', 'ocurrence_time', 'reporting_department', 
        'notified_department', 'patient_involved'
    )
    search_fields = ('reporting_department__name', 'notified_department__name')
    list_filter = ('ocurrence_date', 'patient_involved')
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


@admin.register(Metas)
class MetasAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('id', 'name',)
    ordering = ('id',)


@admin.register(OcurrenceDescription)
class OcurrenceDescriptionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('id', 'name',)
    ordering = ('id',)


@admin.register(ResponseOcurrence)
class ResponseOcurrenceAdmin(admin.ModelAdmin):
    list_display = (
        'ocurrence', 'meta', 'description', 
        'send_manager', 'event_investigation', 
        'ocurrence_classification', 'damage_classification', 
        'incident_classification',
    )
    search_fields = (
        'ocurrence', 'meta', 'send_manager', 'event_investigation',
    )
    list_filter = ('ocurrence', 'meta', 'send_manager', 'event_investigation',)
    date_hierarchy = 'created_at'
    ordering = ('created_at',)
