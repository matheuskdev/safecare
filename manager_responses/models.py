from django.db import models
from responses.models.response_ocurrence_models import ResponseOcurrence
from utils import mixins


class ManagerResponse(
    mixins.TimestampModelMixin,
    mixins.OwnerModelMixin
):
    """
    Model representing the response of a manager to an occurrence.

    Fields:
        response_ocurrence (ForeignKey): The occurrence response to which the manager is responding.
        response_text (TextField): The response text provided by the manager.
    """
    response_ocurrence = models.ForeignKey(
        ResponseOcurrence,
        on_delete=models.CASCADE,
        related_name='manager_responses'
    )
    response_text = models.TextField(
        help_text="Resposta do Gestor"
    )


    class Meta:
        verbose_name: str = 'Resposta do Gestor'
        verbose_name_plural: str = 'Respostas dos Gestores'
        ordering: list = ['created_at']
        indexes: list[models.Index] = [
            models.Index(fields=['response_ocurrence'])
        ]

    def __str__(self) -> str:
        return f"""
        Resposta do Gestor {self.owner.username}
        para {self.response_ocurrence.pk}
        """
