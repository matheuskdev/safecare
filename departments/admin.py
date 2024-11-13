from django.contrib import admin

from . import forms
from .models import Department


class DepartmentAdmin(admin.ModelAdmin):
    """
    Admin interface for the Department model.

    This class customizes the display, search, filter, and ordering
    options for departments in the Django admin interface.
    It also includes a custom save behavior to automatically assign
    the owner as the user who created the department.
    """

    form = forms.DepartmentForm
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
        "owner",
    )
    search_fields = ("name",)
    list_filter = (
        "name",
        "created_at",
    )
    ordering = ("-created_at",)
    date_hierarchy = "created_at"
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "description",
                )
            },
        ),
        (
            "Dates",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )

    def save_model(self, request, obj, form, change):
        """
        Override the save method to assign the owner field.

        Sets the owner of the department as the user who created it,
        but only on initial creation (not on updates).

        Args:
            request: The HTTP request object.
            obj: The Department instance being saved.
            form: The form instance with cleaned data.
            change: Boolean indicating if the object is being changed.
        """
        if not change:  # If this is a new object
            obj.owner = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Department, DepartmentAdmin)
