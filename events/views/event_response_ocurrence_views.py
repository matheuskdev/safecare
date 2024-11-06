from typing import Any

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from events.models.event_ocurrence_models import EventOcurrence
from events.models.response_ocurrence_models import ResponseOcurrence


class EventResponseOcurrenceCreateView(CreateView):
    """
    View to create a response for an event occurrence.

    This view handles the creation of a response to an event occurrence. It first retrieves
    the corresponding event occurrence based on the provided `ocurrence_id`, then associates
    the response with that occurrence before saving the response.

    Attributes:
        model (ResponseOcurrence): The model used to create the response for an event occurrence.
        form_class (str): The form class used to handle the response input (referred by string).
        template_name (str): The name of the template used to render the response form.
        success_url (str): The URL to redirect to after successfully submitting the form.

    Methods:
        dispatch(request, *args, **kwargs):
            Retrieves the event occurrence corresponding to the provided `ocurrence_id`
            before processing the request.

        form_valid(form):
            Associates the response with the retrieved event occurrence and then saves it.

    """
    model = ResponseOcurrence
    form_class = 'EventResponseOcurrenceForm'
    template_name = 'response/events_form.html'
    success_url = reverse_lazy('response_success')

    def dispatch(self, request, *args, **kwargs):
        """
        Retrieves the event occurrence to associate the response with.

        Args:
            request (HttpRequest): The incoming HTTP request.
            *args: Additional positional arguments.
            **kwargs: Keyword arguments containing `ocurrence_id` to retrieve the event occurrence.

        Returns:
            HttpResponse: The response after dispatching the request.
        """
        # Recupera a ocorrência antes de criar a resposta
        self.ocurrence = get_object_or_404(
            EventOcurrence, id=kwargs['ocurrence_id']
        )
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Associates the response with the retrieved event occurrence and saves it.

        Args:
            form (EventResponseOcurrenceForm): The form that has been submitted and validated.

        Returns:
            HttpResponse: The response to be sent after successfully saving the form.
        """
        # Associa a resposta com a ocorrência recuperada
        form.instance.ocurrence = self.ocurrence
        return super().form_valid(form)
