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
    """
    View for listing departments with optional filtering by name.

    This view retrieves and displays a paginated list of departments. It allows
    filtering departments by their name through a query parameter (`name`), and
    requires the user to be logged in with the necessary permissions.

    Attributes:
        model (models.Department): The model representing a department.
        template_name (str): The name of the template to render for this view.
        context_object_name (str): The name of the context variable to be used in the template.
        paginate_by (int): The number of departments to display per page.
        permission_required (str): The permission required to access this view.

    Methods:
        get_queryset():
            Filters departments based on the query parameter `name` if provided.
    """

    model = models.Department
    template_name = "department_list.html"
    context_object_name = "departments"
    paginate_by = 5
    permission_required = "departments.view_department"

    def get_queryset(self):
        """
        Retrieves a filtered list of departments based on the query parameter `name`.

        Returns:
            queryset: A queryset of departments, optionally filtered by the `name` query parameter.
        """
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
    """
    View for creating a new department.

    This view provides a form to create a new department. Only users with the
    appropriate permissions can create a department. After a successful form submission,
    the user is redirected to the department list.

    Attributes:
        model (models.Department): The model for the department.
        template_name (str): The template used to render the form for creating a department.
        form_class (forms.DepartmentForm): The form class used to handle department creation.
        success_url (str): The URL to redirect to after a successful creation.
        permission_required (str): The permission required to create a department.

    Methods:
        form_valid(form):
            Saves the department instance after validating the form and redirects to the success URL.
    """

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
    """
    View for displaying the details of a specific department.

    This view retrieves a specific department based on its ID and displays its details.
    Only users with the appropriate permissions can view the department details.

    Attributes:
        model (models.Department): The model for the department.
        template_name (str): The template used to render the department details.
        context_object_name (str): The name of the context variable to be used in the template.
        permission_required (str): The permission required to access this view.

    Methods:
        get_context_data():
            Provides additional context data, such as department details.
    """

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
    """
    View for updating an existing department.

    This view allows updating the details of an existing department. After a successful update,
    the user is redirected to the department list. Only users with the appropriate permissions
    can update a department.

    Attributes:
        model (models.Department): The model for the department.
        template_name (str): The template used to render the form for updating a department.
        form_class (forms.DepartmentForm): The form class used to handle department updates.
        success_url (str): The URL to redirect to after a successful update.
        permission_required (str): The permission required to update a department.

    Methods:
        form_valid(form):
            Saves the updated department instance after validating the form and redirects to the success URL.
    """

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
    """
    View for deleting a department.

    This view allows for the soft deletion of a department. After a successful deletion,
    the user is redirected to the department list. Only users with the appropriate permissions
    can delete a department.

    Attributes:
        model (models.Department): The model for the department.
        template_name (str): The template used to confirm the deletion of a department.
        success_url (str): The URL to redirect to after a successful deletion.
        permission_required (str): The permission required to delete a department.

    Methods:
        form_valid(form):
            Performs the soft deletion of the department and redirects to the success URL.
    """

    model = models.Department
    template_name = "department_confirm_delete.html"
    success_url = reverse_lazy("departments:department_list")
    permission_required = "departments.delete_department"
