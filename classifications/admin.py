from django.contrib import admin

from .models import (
    DamageClassification,
    IncidentClassification,
    OcurrenceClassification,
)


@admin.register(IncidentClassification)
class IncidentClassificationAdmin(admin.ModelAdmin):
    list_display = ('classification',)
    search_fields = ('classification',)
    list_filter = ('classification',)
    date_hierarchy = 'created_at'
    ordering = ('classification',)


@admin.register(OcurrenceClassification)
class OcurrenceClassificationAdmin(admin.ModelAdmin):
    list_display = ('classification',)
    search_fields = ('classification',)
    list_filter = ('classification',)
    date_hierarchy = 'created_at'
    ordering = ('classification',)


@admin.register(DamageClassification)
class DamageClassificationAdmin(admin.ModelAdmin):
    list_display = ('classification',)
    search_fields = ('classification',)
    list_filter = ('classification',)
    date_hierarchy = 'created_at'
    ordering = ('classification',)
