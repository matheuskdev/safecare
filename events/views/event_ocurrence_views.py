""" Module views for Events """

from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from events.forms.event_ocurrence_forms import EventOcurrenceForm
from events.forms.event_patient_forms import EventPatientForm
from events.models.event_ocurrence_models import EventOcurrence


class EventOcurrenceCreateView(CreateView):
    """
    View to create an event occurrence notification.

    This view is responsible for handling the creation of a new event
    occurrence.
    It displays a form to submit event details, and optionally the details of
    a patient involved in the event.
    Once the form is validated and submitted, it redirects the user to a
    success page.

    Attributes:
        model (EventOcurrence): The model used by the view to create an event
        occurrence.
        form_class (EventOcurrenceForm): The form class used to handle the
        event occurrence input.
        template_name (str): The name of the template used to render the form.
        success_url (str): The URL to redirect to after successfully
        submitting the form.

    Methods:
        get_context_data(**kwargs):
            Returns the context data to be rendered in the template,
            including the patient form and the current date.

        form_valid(form):
            Validates the event occurrence form and the patient form
            (if applicable), then saves the event occurrence.

        form_invalid(form):
            Handles invalid form submissions and re-renders the form with
            error messages.

        get_success_url():
            Returns the URL to redirect to after successfully creating the
            event occurrence.
    """

    model = EventOcurrence
    form_class = EventOcurrenceForm
    template_name = "event/events_form.html"
    success_url = reverse_lazy("events:eventocurrence_success")

    def get_context_data(self, **kwargs: dict) -> dict[str, dict]:
        """
        Adds additional context data to the form view, including a patient form and the current date.

        Args:
            **kwargs: Additional keyword arguments passed to the context.

        Returns:
            context: The context data including the patient form and current date.
        """
        context: dict = super().get_context_data(**kwargs)
        context["patient_form"] = EventPatientForm(self.request.POST or None)
        context["current_date"] = datetime.now()
        return context

    def form_valid(self, form) -> HttpResponse:
        """
        Handles valid form submission. If the patient involved is specified, it validates and saves the patient form.

        Args:
            form (EventOcurrenceForm): The event occurrence form that has been submitted.

        Returns:
            HttpResponse: The response to be sent after successfully saving the form.
        """
        context = self.get_context_data()
        patient_form = context["patient_form"]
        if form.cleaned_data.get("patient_involved"):
            if patient_form.is_valid():
                patient = patient_form.save()
                form.instance.patient = patient
            else:
                return self.form_invalid(form)

        return super().form_valid(form)

    def form_invalid(self, form) -> HttpResponse:
        """
        Handles invalid form submissions, rendering the form with errors.

        Args:
            form (EventOcurrenceForm): The invalid form that was submitted.

        Returns:
            HttpResponse: The response to be sent after the form is invalid.
        """

    def get_success_url(self) -> str:
        """
        Returns the URL to redirect to after successfully submitting the form.

        Returns:
            str: The URL for the success page, including the ID of the created event occurrence.
        """
        return reverse("events:eventocurrence_success", kwargs={"pk": self.object.id})


class EventSucessTemplateView(TemplateView):
    """
    View to display the success page after an event occurrence is submitted.

    This view is responsible for showing a success message with the details of the
    event occurrence after it has been successfully created. It fetches the event
    from the database using the primary key provided in the URL.

    Attributes:
        template_name (str): The name of the template used to render the success page.

    Methods:
        get_context_data(**kwargs):
            Returns the context data to be rendered in the success page, including the event details.
    """

    template_name = "event/event_sucess.html"

    def get_context_data(self, **kwargs: dict[str]) -> dict[str]:
        """
        Adds the event details to the context for rendering the success page.

        Args:
            **kwargs: Additional keyword arguments passed to the context.

        Returns:
            dict: The context data including the event details.
        """
        context = super().get_context_data(**kwargs)
        event = get_object_or_404(EventOcurrence, pk=self.kwargs.get("pk"))
        context["event"] = event
        # context['pk'] = self.kwargs.get('pk')
        return context


class EventListView(ListView):
    model = EventOcurrence
    template_name = "event/events_list.html"
    context_object_name = "events"
    paginate_by = 5

    def get_queryset(self):
        return EventOcurrence.objects.filter(response_ocurrence__isnull=True)
