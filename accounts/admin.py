from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    """
    Custom admin interface for the User model.

    Inherits from:
        BaseUserAdmin: The default user admin from Django's auth app.

    Model:
        User (class): The custom User model.

    List display:
        - email: User's email address.
        - username: User's username.
        - first_name: User's first name.
        - last_name: User's last name.
        - is_staff: Whether the user can access the admin site.
        - is_active: Whether the user is active.

    Fieldsets:
        - None: Fields for email, password, and departments.
        - Personal Information: Fields for username, first name, last name, bio, website, and profile picture.
        - Permissions: Fields for active status, staff status, superuser status, groups, and user permissions.
        - Important Dates: Fields for last login and account creation date.

    Add fieldsets:
        - None: Fields for email, username, password1, and password2.

    Search Fields:
        - email: Search by user's email address.
        - username: Search by user's username.

    Ordering:
        - email: Order by email address.

    Read-only fields:
        - last_login: The last time the user logged in.
        - date_joined: The date when the user account was created.
    """

    model = User
    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )

    fieldsets = (
        (None, {"fields": ("email", "password", "departments")}),
        (
            "Informações Pessoais",
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "bio",
                    "website",
                    "profile_picture",
                )
            },
        ),
        (
            "Permissões",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Datas Importantes", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )
    search_fields = ("email", "username")
    ordering = ("email",)
    readonly_fields = (
        "last_login",
        "date_joined",
    )
