from django.contrib import admin

from responses.models.metas_models import Metas
from responses.models.ocurrence_description_models import OcurrenceDescription
from responses.models.response_ocurrence_models import ResponseOcurrence


@admin.register(Metas)
class MetasAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = (
        "id",
        "name",
    )
    ordering = ("id",)


@admin.register(OcurrenceDescription)
class OcurrenceDescriptionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = (
        "id",
        "name",
    )
    ordering = ("id",)


@admin.register(ResponseOcurrence)
class ResponseOcurrenceAdmin(admin.ModelAdmin):
    list_display = (
        "ocurrence",
        "meta",
        "description",
        "send_manager",
        "event_investigation",
        "ocurrence_classification",
        "damage_classification",
        "incident_classification",
    )
    search_fields = (
        "ocurrence",
        "meta",
        "send_manager",
        "event_investigation",
    )
    list_filter = (
        "ocurrence",
        "meta",
        "send_manager",
        "event_investigation",
    )
    date_hierarchy = "created_at"
    ordering = ("created_at",)
