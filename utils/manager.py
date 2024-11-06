from django.db import models


class NonDeletedManager(models.Manager):
    """
    Custom Manager to filter out objects that are marked as deleted.

    This manager overrides the default `get_queryset` method to exclude 
    objects where the `is_deleted` attribute is set to True. It is 
    useful for implementing soft delete functionality in your models.

    Inherits from:
        models.Manager: The base manager class from Django.

    Methods:
        get_queryset(): Returns a queryset that filters out deleted objects.
    """

    def get_queryset(self):
        """
        Return a queryset that excludes objects marked as deleted.

        This method filters the queryset to include only objects where 
        `is_deleted` is False.

        Returns:
            QuerySet: A queryset of non-deleted objects.
        """
        return super().get_queryset().filter(is_deleted=False)
