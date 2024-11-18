"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from typing import Literal

from django.urls import path

from events.views.event_ocurrence_views import (
    EventListView,
    EventOcurrenceCreateView,
    EventOcurrenceDataView,
    EventSucessTemplateView,
    EventOcurrenceDeleteView,
)

app_name: Literal["events"] = "events"

urlpatterns = [
    path("", EventOcurrenceCreateView.as_view(), name="eventocurrence_create"),
    path(
        "events/<int:pk>/sucess/",
        EventSucessTemplateView.as_view(),
        name="eventocurrence_success",
    ),
    path(
        "events/list/no_response/",
        EventListView.as_view(),
        name="eventocurrence_list",
    ),
    path(
        "events/<int:pk>/delete/",
        EventOcurrenceDeleteView.as_view(),
        name="eventocurrence_delete"
    ),
    path(
        "events/get_event_data/<int:pk>/",
        EventOcurrenceDataView.as_view(),
        name="get_event_data",
    ),
]
