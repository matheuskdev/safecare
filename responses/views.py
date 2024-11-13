"""Module to handle response creation for an event occurrence."""

from typing import Any

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from events.models.event_ocurrence_models import EventOcurrence
from events.models.event_patient_models import EventPatient
from responses.forms import ResponseOcurrenceForm
from responses.models.response_ocurrence_models import ResponseOcurrence


class EventResponseOcurrenceCreateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    FormView,
):
    """
    View to create a response for an event occurrence.

    This view handles the creation of a response for a specific event occurrence.
    It retrieves the event occurrence and associates the response with it.
    Only users with appropriate permissions can access this view.

    Inherits from:
        LoginRequiredMixin: Ensures the user is authenticated.
        PermissionRequiredMixin: Ensures the user has the correct permissions.
        FormView: Handles form rendering and processing.

    Attributes:
        model (ResponseOcurrence): The model associated with this form view.
        form_class (ResponseOcurrenceForm): The form class for creating a response.
        template_name (str): The template to render for this view.
        success_url (str): The URL to redirect to upon successful form submission.
        permission_required (str): Permission required to access this view.
        ocurrence (EventOcurrence): The event occurrence being responded to.
        patient (EventPatient): The patient associated with the event occurrence.
    """

    model = ResponseOcurrence
    form_class = ResponseOcurrenceForm
    template_name = "response/events_form.html"
    success_url = reverse_lazy("events:response_success")
    permission_required = "events.add_responseocurrence"

    def __init__(self, **kwargs: Any) -> None:
        """
        Initializes the EventResponseOcurrenceCreateView with optional arguments.

        Args:
            **kwargs (dict): Additional arguments to pass to the parent class.
        """
        self.ocurrence: EventOcurrence = None
        self.patient: EventPatient = None

    def dispatch(self, request, *args, **kwargs):
        """
        Retrieves the event occurrence corresponding to the provided `ocurrence_id`
        before processing the request.

        Args:
            request (HttpRequest): The request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponse: The response to proceed with the request.
        """
        ocurrence_id = self.kwargs.get("pk")
        self.ocurrence = get_object_or_404(EventOcurrence, pk=ocurrence_id)

        if self.ocurrence.patient_involved:
            patient_id = self.ocurrence.patient_id
            self.patient = get_object_or_404(EventPatient, pk=patient_id)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        """
        Adds additional context for rendering the template, including the event
        occurrence and any existing responses.

        Args:
            **kwargs (dict): Additional context data.

        Returns:
            dict: Context data to be used in the template.
        """
        context: dict = super().get_context_data(**kwargs)
        context["ocurrence"] = self.ocurrence
        context["responses"] = ResponseOcurrence.objects.filter(
            ocurrence=self.ocurrence
        )
        if self.ocurrence.patient_involved:
            context["patient"] = self.patient
        return context

    def form_valid(self, form):
        """
        Associates the response with the retrieved event occurrence and saves it.

        This method is called when the submitted form is valid. It links the
        response to the current event occurrence and assigns the current user
        as the owner of the response.

        Args:
            form (ResponseOcurrenceForm): The validated form instance.

        Returns:
            HttpResponse: The response to proceed with after form submission.
        """
        response = form.save(commit=False)
        response.ocurrence = self.ocurrence
        response.owner = self.request.user
        response.save()
        print(response)
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Handles invalid form submissions by displaying form errors for debugging.

        This method renders the template with the current context and form
        errors if the form submission is invalid.

        Args:
            form (ResponseOcurrenceForm): The form instance with validation errors.

        Returns:
            HttpResponse: The response with rendered template and form errors.
        """
        print("Form inválido:", form.errors)
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get_success_url(self):
        """
        Returns the URL to redirect to upon successful form submission.

        Returns:
            str: The success URL.
        """
        return reverse_lazy("events:response_success")
