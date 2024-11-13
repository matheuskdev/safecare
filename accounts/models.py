from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import MinLengthValidator
from django.db import models

from departments.models import Department
from utils import regex


class CustomUserManager(BaseUserManager):
    """
    Custom manager for the User model.

    This manager provides methods to create regular users and superusers.

    Methods:
        create_user(email, password, **extra_fields):
            Creates and returns a regular user with an email, password, and extra fields.

        create_superuser(email, password, **extra_fields):
            Creates and returns a superuser with an email, password, and extra fields.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email, password, and extra fields.

        Args:
            email (str): The email address of the user.
            password (str, optional): The password for the user. Defaults to None.
            **extra_fields: Additional fields to be passed to the user model.

        Raises:
            ValueError: If no email is provided.

        Returns:
            User: The created user object.
        """
        if not email:
            raise ValueError("O campo de email deve ser preenchido.")

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email, password, and extra fields.

        Args:
            email (str): The email address of the superuser.
            password (str, optional): The password for the superuser. Defaults to None.
            **extra_fields: Additional fields to be passed to the user model.

        Returns:
            User: The created superuser object.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model for the application.

    This model extends Django's AbstractBaseUser and PermissionsMixin to provide
    additional fields and functionality, including support for email as the
    primary identifier and customizable user attributes.

    Attributes:
        email (EmailField): The user's email address, which must be unique.
        username (CharField): The user's username, which must be unique and have
                              a minimum length of 4 characters.
        first_name (CharField): The user's first name, optional.
        last_name (CharField): The user's last name, optional.
        bio (TextField): A brief biography of the user, optional.
        website (URLField): The user's website, optional.
        profile_picture (ImageField): The user's profile picture, optional.
        phone (CharField): The user's phone number, optional, validated using a regex pattern.
        departments (ManyToManyField): The departments the user belongs to, optional.
        is_active (BooleanField): Whether the user's account is active. Default is True.
        is_staff (BooleanField): Whether the user has staff permissions. Default is False.
        is_superuser (BooleanField): Whether the user is a superuser. Default is False.
        last_login (DateTimeField): The date and time the user last logged in, optional.
        date_joined (DateTimeField): The date and time the user joined, automatically set.

    Methods:
        __str__():
            Returns the user's email address as a string representation.

    Meta:
        ordering (list): The default ordering of users by email.
        verbose_name (str): A human-readable singular name for the model.
        verbose_name_plural (str): A human-readable plural name for the model.
        indexes (list): Database index on the `email` field to optimize queries.
        constraints (list): Unique constraints for `email` and `username`.

    Custom Manager:
        objects (CustomUserManager): Custom manager for creating users and superusers.
    """

    email = models.EmailField(unique=True)
    username = models.CharField(
        max_length=18,
        unique=True,
        validators=[
            MinLengthValidator(
                limit_value=4,
                message="O nome de usuário deve ter no mínimo 4 caracteres.",
            )
        ],
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True, null=True, max_length=1012)
    website = models.URLField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, null=True
    )
    phone = models.CharField(
        max_length=20,
        validators=[regex.phone_regex],
        help_text="Número de telefone/celular",
        null=True,
        blank=True,
    )

    departments = models.ManyToManyField(
        Department, related_name="users", blank=True
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        """Meta options for the User model."""

        ordering = ["email"]
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        indexes = [
            models.Index(fields=["email"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["email"], name="unique_user_email"
            ),
            models.UniqueConstraint(
                fields=["username"], name="unique_user_username"
            ),
        ]

    def __str__(self):
        """
        Return the user's email address as a string.

        This method provides a string representation of the user, typically used
        in admin interfaces and other textual outputs.

        Returns:
            str: The user's email address.
        """
        return self.email
