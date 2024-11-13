from django.contrib import admin

from .models import (
    DamageClassification,
    IncidentClassification,
    OcurrenceClassification,
)


@admin.register(IncidentClassification)
class IncidentClassificationAdmin(admin.ModelAdmin):
    """
    Admin interface for managing IncidentClassification instances.

    Provides list display, search, and filtering capabilities for the
    classification field, enabling efficient management of incident classifications.
    Configures ordering by classification and uses created_at for date hierarchy.
    """

    list_display = ("classification",)
    search_fields = ("classification",)
    list_filter = ("classification",)
    date_hierarchy = "created_at"
    ordering = ("classification",)


@admin.register(OcurrenceClassification)
class OcurrenceClassificationAdmin(admin.ModelAdmin):
    """
    Admin interface for managing OcurrenceClassification instances.

    Offers a streamlined display and filtering for the classification field,
    allowing administrators to easily search, sort, and organize occurrence
    classifications. Ordered by classification with a date hierarchy on created_at.
    """

    list_display = ("classification",)
    search_fields = ("classification",)
    list_filter = ("classification",)
    date_hierarchy = "created_at"
    ordering = ("classification",)


@admin.register(DamageClassification)
class DamageClassificationAdmin(admin.ModelAdmin):
    """
    Admin interface for managing DamageClassification instances.

    Configures list display, search fields, and filters for the classification field,
    supporting efficient management and sorting by classification, with created_at
    set for date-based filtering.
    """

    list_display = ("classification",)
    search_fields = ("classification",)
    list_filter = ("classification",)
    date_hierarchy = "created_at"
    ordering = ("classification",)
