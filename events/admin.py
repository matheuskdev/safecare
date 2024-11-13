from django.contrib import admin

from events.models.event_ocurrence_models import EventOcurrence
from events.models.event_patient_models import EventPatient
from events.models.gender_models import Gender
from events.models.race_models import Race


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    """Admin view for managing Gender model entries."""

    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("id", "name")
    ordering = ("id",)


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    """Admin view for managing Race model entries."""

    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("id", "name")
    ordering = ("id",)


@admin.register(EventPatient)
class EventPatientAdmin(admin.ModelAdmin):
    """Admin view for managing EventPatient model entries."""

    list_display = (
        "patient_name",
        "attendance",
        "record",
        "birth_date",
        "internment_date",
    )
    search_fields = ("patient_name", "attendance", "record")
    list_filter = ("internment_date", "birth_date")
    date_hierarchy = "internment_date"
    ordering = ("patient_name",)


@admin.register(EventOcurrence)
class EventOcurrenceAdmin(admin.ModelAdmin):
    """
    Admin view for managing EventOcurrence model entries.

    Provides custom display of occurrences with patient involvement, 
    related department information, and conditional read-only fields.
    """

    list_display = (
        "ocurrence_date",
        "ocurrence_time",
        "reporting_department",
        "notified_department",
        "patient_involved",
        "get_patient_name",
    )
    search_fields = ("reporting_department__name", "notified_department__name")
    list_filter = ("ocurrence_date", "patient_involved")
    date_hierarchy = "ocurrence_date"
    ordering = ("ocurrence_date",)

    # Exibir campos relacionados ao paciente quando for marcado como envolvido
    def get_readonly_fields(self, request, obj=None):
        """
        Sets 'patient' field as read-only if a patient is involved in the occurrence.

        Args:
            request (HttpRequest): The request object.
            obj (EventOcurrence, optional): The occurrence being edited.
        
        Returns:
            list: Fields that should be read-only.
        """
        if obj and obj.patient_involved:
            return super().get_readonly_fields(request, obj) + ("patient",)
        return super().get_readonly_fields(request, obj)

    def get_patient_name(self, obj):
        """
        Retrieves the name of the patient involved in the occurrence, if any.

        Args:
            obj (EventOcurrence): The occurrence instance.

        Returns:
            str: The patient's name or 'Nenhum Paciente' if none is associated.
        """
        return obj.patient.patient_name if obj.patient else "Nenhum Paciente"

    get_patient_name.short_description = "Paciente Envolvido"
