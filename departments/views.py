from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from utils import mixins

from . import forms, models


class DepartmentListView(
    mixins.DepartmentListFilterMixin,
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ListView,
):
    model = models.Department
    template_name = "department_list.html"
    context_object_name = "departments"
    paginate_by = 5
    permission_required = "departments.view_department"

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")

        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class DepartmentCreateView(
    LoginRequiredMixin,
    mixins.OwnerUserMixin,
    PermissionRequiredMixin,
    CreateView,
):
    model = models.Department
    template_name = "department_form.html"
    form_class = forms.DepartmentForm
    success_url = reverse_lazy("departments:department_list")
    permission_required = "departments.add_department"


class DepartmentDetailView(
    mixins.DepartmentPermissionMixin,
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DetailView,
):
    model = models.Department
    template_name = "department_detail.html"
    context_object_name = "department"
    permission_required = "departments.view_department"


class DepartmentUpdateView(
    mixins.DepartmentPermissionMixin,
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UpdateView,
):
    model = models.Department
    template_name = "department_form.html"
    form_class = forms.DepartmentForm
    success_url = reverse_lazy("departments:department_list")
    permission_required = "departments.change_department"


class DepartmentDeleteView(
    mixins.SoftDeleteViewMixin,
    mixins.DepartmentPermissionMixin,
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DeleteView,
):
    model = models.Department
    template_name = "department_confirm_delete.html"
    success_url = reverse_lazy("departments:department_list")
    permission_required = "departments.delete_department"
