from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy

from . import manager


class TimestampModelMixin(models.Model):
    """
    Abstract model mixin that provides self-managed timestamp fields.

    This mixin adds `created_at` and `updated_at` fields to any model
    that inherits from it, automatically setting these fields when the
    model instance is created or updated.

    Attributes:
        created_at (DateTimeField): The timestamp when the object was created.
        updated_at (DateTimeField): The timestamp when the object was last updated.

    Meta:
        abstract: This is an abstract base class and won't be used to create any database table.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteModelMixin(models.Model):
    """
    Abstract model mixin for soft delete functionality.

    This mixin adds an `is_deleted` field and methods for soft deleting
    and restoring objects. It also includes a custom manager to filter
    out deleted objects by default.

    Attributes:
        is_deleted (BooleanField): A flag indicating whether the object has been soft deleted.
        objects (NonDeletedManager): Custom manager that filters out deleted objects.
        all_objects (models.Manager): Default manager that includes all objects, regardless of deletion status.

    Methods:
        soft_delete(): Marks the object as deleted and saves it.
        restore(): Marks the object as not deleted and saves it.

    Meta:
        abstract: This is an abstract base class and won't be used to create any database table.
    """

    is_deleted = models.BooleanField(default=False)
    objects = manager.NonDeletedManager()
    all_objects = models.Manager()

    def soft_delete(self):
        """Marks the object as deleted and saves it."""
        self.is_deleted = True
        self.save()

    def restore(self):
        """Restores the object by marking it as not deleted and saves it."""
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True


class SoftDeleteViewMixin:
    """
    View mixin that overrides the delete method to perform a soft delete.

    This mixin is intended for use with class-based views. It modifies
    the default behavior of the delete method to use soft delete instead
    of permanently removing the object from the database.

    Methods:
        delete(request, *args, **kwargs): Performs a soft delete on the object.
        post(request, *args, **kwargs): Handles POST requests and calls delete.
    """

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.soft_delete()
        return HttpResponseRedirect(self.get_success_url())

    def post(self, request, *args, **kwargs):
        """Handles POST requests and calls the delete method."""
        return self.delete(request, *args, **kwargs)


class OwnerModelMixin(models.Model):
    """
    Abstract model mixin that adds an `owner` field.

    This mixin associates the model instance with a user, making it
    possible to track ownership of objects.

    Attributes:
        owner (ForeignKey): A foreign key to the user who owns the object.

    Meta:
        abstract: This is an abstract base class and won't be used to create any database table.
    """

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    class Meta:
        abstract = True


class OwnerUserMixin:
    """
    View mixin that assigns the current user as the owner of a model instance.

    This mixin is used to automatically set the `owner` attribute of
    a model instance when a form is successfully validated.

    Methods:
        form_valid(form): Sets the owner to the current user and calls the parent method.
    """

    def form_valid(self, form):
        """Assigns the current user to the owner field of the model instance."""
        form.instance.owner = self.request.user
        return super().form_valid(form)


class DepartmentListFilterMixin:
    """
    Mixin to filter querysets based on the user's department.

    This mixin filters objects based on the user's department. If the
    user belongs to the "Administração" department, all objects are
    returned. Otherwise, only objects associated with the user's
    department or owned by the user are included.

    Methods:
        get_queryset(): Returns a filtered queryset based on the user's department.
        handle_no_permission(): Redirects the user to the home page with an error message if permission is denied.
    """

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()

        if queryset is None:
            queryset = self.model.objects.none()

        queryset = queryset.filter(is_deleted=False)

        if user.departments.filter(name="Administração").exists():
            return queryset

        if hasattr(self.model, "department"):
            return queryset.filter(
                Q(owner=user)
                | Q(owner__departments__in=user.departments.all())
                | Q(department__in=user.departments.all())
            ).distinct()

        return queryset.filter(
            Q(owner=user) | Q(owner__departments__in=user.departments.all())
        ).distinct()

    def handle_no_permission(self):
        """Handles cases where the user lacks permission to access a resource."""
        if self.request.user.is_authenticated:
            messages.error(
                self.request,
                "Você não tem permissão para acessar a página anterior. Faça seu login!",
            )
            return redirect(reverse_lazy("home"))
        else:
            return super().handle_no_permission()


class DepartmentPermissionMixin:
    """
    Mixin to check if the user has permission to access an object.

    This mixin ensures that the user can only access objects they own
    or are associated with through their department. Users in the
    "Administração" department have access to all objects.

    Methods:
        dispatch(request, *args, **kwargs): Checks access permission and returns the appropriate response.
    """

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        User = get_user_model()
        try:
            user_profile = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            messages.error(request, "Perfil do usuário não encontrado.")
            return HttpResponseRedirect(reverse("home"))

        is_owner = request.user == obj.owner
        is_department_admin = (
            "Administração"
            in user_profile.departments.values_list("name", flat=True)
        )
        is_in_department = hasattr(self.model, "department") and str(
            obj.department
        ) in request.user.departments.values_list("name", flat=True)
        is_department_in_owner_dep = (
            request.user.departments.values_list
            in obj.owner.departments.values_list("name", flat=True)
        )

        if not (
            is_owner
            or is_department_admin
            or is_in_department
            or is_department_in_owner_dep
        ):
            messages.error(
                request,
                "Você não tem nível de permissão para acessar este recurso.",
            )
            return HttpResponseRedirect(reverse("home"))

        return super().dispatch(request, *args, **kwargs)
