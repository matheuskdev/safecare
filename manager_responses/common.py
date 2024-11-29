from typing import Any, Optional
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)

from events.models.event_ocurrence_models import EventOcurrence
from events.models.event_patient_models import EventPatient
from responses.models.response_ocurrence_models import ResponseOcurrence


class GenericResponseFormView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    FormView,
):
    model = None
    form_class = None
    template_name: str = ''
    success_url = None
    permission_required = None
    context_responses_model = None
    success_url_name = None
    response_ocurrence_id = None

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.ocurrence: Optional[EventOcurrence] = None
        self.patient: Optional[EventPatient] = None

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """
        Retrieves the OCC corresponding to the provided `ocurrence_id`
        before processing the request.
        """
        self.response_ocurrence_id: int = self.kwargs.get("pk")
        self.response_ocurrence: ResponseOcurrence = get_object_or_404(
            ResponseOcurrence, id=self.response_ocurrence_id
        )

        self.ocurrence = get_object_or_404(
            EventOcurrence,
            pk=self.response_ocurrence.ocurrence.id
        )

        if self.ocurrence.patient_involved:
            patient_id = self.ocurrence.patient.id
            self.patient = get_object_or_404(EventPatient, pk=patient_id)

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        """
        Adds additional context for rendering the template.
        """
        context: dict[str, Any] = super().get_context_data(**kwargs)
        context["ocurrence"] = self.ocurrence
        context["response_ocurrence"] = self.response_ocurrence
        if self.ocurrence.patient_involved:  # type: ignore
            context["patient"] = self.patient
        return context

    def form_valid(self, form) -> HttpResponse:
        """
        Handles valid form submissions.
        """
        response = form.save(commit=False)
        response.ocurrence = self.ocurrence
        response.owner = self.request.user
        response.save()
        messages.success(
            self.request,
            MessageDescription.get_message_description('SUCCESS')
        )
        return super().form_valid(form)

    def form_invalid(self, form) -> HttpResponse:
        """
        Handles invalid form submissions.
        """
        print("Form inválido:", form.errors)
        context: dict[str, Any] = self.get_context_data(form=form)
        messages.error(
            self.request,
            MessageDescription.get_message_description('ERROR')
        )
        return self.render_to_response(context)

    def get_success_url(self):
        """
        Returns the URL to redirect to upon successful form submission.
        """
        if not self.success_url:
            raise ValueError("A URL de sucesso não foi definida.")
        return reverse_lazy(self.success_url)


class MessageDescription:
    """
    Class to store messages to be displayed to the user.

    Attributes:

        ERROR (str): Ocorreu um erro ao processar a solicitação.
        SUCCESS (str): Solicitação processada com sucesso.
        WARNING (str): Atenção:
        INFO (str): Informação:

    Methods:

        get_message_description(message_type: str) -> str:
            Returns the message description corresponding to the provided `message_type`.

    """
    ERROR = "Ocorreu um erro ao processar a solicitação."
    SUCCESS = "Solicitação processada com sucesso."
    WARNING = "Atenção: "
    INFO = "Informação: "

    @staticmethod
    def get_message_description(message_type: str) -> str:
        """
        Returns the message description corresponding to the provided `message_type`.
        """
        return getattr(
            MessageDescription,
            message_type,
            "Tipo de mensagem não encontrado."
        )
