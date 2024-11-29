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
from django.urls.resolvers import URLPattern

from .views import ManagerResponseFormView

app_name: Literal["manager_responses"] = "manager_responses"

urlpatterns: list[URLPattern] = [
    path(
        "manager_response/<int:pk>/",
        ManagerResponseFormView.as_view(),
        name="manager_response_create",
    ),
]