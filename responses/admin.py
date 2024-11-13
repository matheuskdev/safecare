from django.contrib import admin

from responses.models.metas_models import Metas
from responses.models.ocurrence_description_models import OcurrenceDescription
from responses.models.response_ocurrence_models import ResponseOcurrence


@admin.register(Metas)
class MetasAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Metas model.

    This configuration customizes how the Metas model is displayed in the
    Django admin interface, providing list display, search, filter, and ordering options.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        search_fields (tuple): Fields to include in the search functionality.
        list_filter (tuple): Fields to include in the filter sidebar.
        ordering (tuple): Default ordering for the admin list view.
    """

    list_display = ("name",)
    search_fields = ("name",)
    list_filter = (
        "id",
        "name",
    )
    ordering = ("id",)


@admin.register(OcurrenceDescription)
class OcurrenceDescriptionAdmin(admin.ModelAdmin):
    """
    Admin configuration for the OcurrenceDescription model.

    Customizes the Django admin interface for the OcurrenceDescription model,
    with display, search, filtering, and ordering options.

    Attributes:
        list_display (tuple): Fields displayed in the admin list view.
        search_fields (tuple): Fields for the search functionality.
        list_filter (tuple): Fields available in the filter sidebar.
        ordering (tuple): Default ordering for the admin list view.
    """

    list_display = ("name",)
    search_fields = ("name",)
    list_filter = (
        "id",
        "name",
    )
    ordering = ("id",)


@admin.register(ResponseOcurrence)
class ResponseOcurrenceAdmin(admin.ModelAdmin):
    """
    Admin configuration for the ResponseOcurrence model.

    Configures the Django admin interface for the ResponseOcurrence model with
    options for display, search, filter, date hierarchy, and ordering.

    Attributes:
        list_display (tuple): Fields displayed in the list view for quick overview.
        search_fields (tuple): Fields for enabling search functionality.
        list_filter (tuple): Fields available in the filter sidebar.
        date_hierarchy (str): Field to use for date-based drill-down navigation.
        ordering (tuple): Default ordering for the list view.
    """

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
