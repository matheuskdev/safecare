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
from django.urls import path

from events.views.event_ocurrence_views import (
    EventOcurrenceCreateView,
    EventSucessTemplateView,
    EventListView,
)
from events.views.event_response_ocurrence_views import (
    EventResponseOcurrenceCreateView,
)

app_name = 'events'

urlpatterns = [
    path('', EventOcurrenceCreateView.as_view(), name='home'),
    path(
        'sucess/<int:pk>/',
        EventSucessTemplateView.as_view(),
        name='event_success'
    ),
    path(
        'response_event/<int:pk>/',
        EventResponseOcurrenceCreateView.as_view(),
        name='response_event_create'
    ),
    path(
        'events/no_response/',
        EventListView.as_view(),
        name='event_no_response'
    )
]
