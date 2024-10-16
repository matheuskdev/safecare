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

from . import views

app_name = "departments"

urlpatterns = [
    path("departments/", views.DepartmentListView.as_view(), name="department_list"),
    path("departments/<int:pk>/", views.DepartmentDetailView.as_view(), name="department_detail"),
    path("departments/create/", views.DepartmentCreateView.as_view(), name="department_create"),
    path(
        "departments/<int:pk>/update/", views.DepartmentUpdateView.as_view(), name="department_update"
    ),
    path(
        "departments/<int:pk>/delete/", views.DepartmentDeleteView.as_view(), name="department_delete"
    ),
]