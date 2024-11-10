from typing import Any

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from events.forms.response_ocurrence_forms import ResponseOcurrenceForm
from events.models.event_ocurrence_models import EventOcurrence
from events.models.event_patient_models import EventPatient
from events.models.response_ocurrence_models import ResponseOcurrence


class EventResponseOcurrenceCreateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    FormView,
):
    """
    View to create a response for an event occurrence.

    This view handles the creation of a response to an event occurrence. It first retrieves
    the corresponding event occurrence based on the provided `ocurrence_id`, then associates
    the response with that occurrence before saving the response.
    """
    model = ResponseOcurrence
    form_class = ResponseOcurrenceForm
    template_name = 'response/events_form.html'
    success_url = reverse_lazy('events:response_success')
    permission_required = "events.add_responseocurrence"

    def dispatch(self, request, *args, **kwargs):
        """
        Retrieves the event occurrence corresponding to the provided `ocurrence_id`
        before processing the request.
        """
        ocurrence_id = self.kwargs.get('pk')
        self.ocurrence = get_object_or_404(EventOcurrence, pk=ocurrence_id)
        
        if self.ocurrence.patient_involved:
            patient_id = self.ocurrence.patient_id
            self.patient = get_object_or_404(EventPatient, pk=patient_id)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        """
        Adds the event occurrence to the context, along with any existing responses.
        """
        context: dict = super().get_context_data(**kwargs)
        context['ocurrence'] = self.ocurrence
        context['responses'] = ResponseOcurrence.objects.filter(ocurrence=self.ocurrence)
        if self.ocurrence.patient_involved: context['patient'] = self.patient
        return context

    def form_valid(self, form):
        """
        Associates the response with the retrieved event occurrence and saves it.
        """
        response = form.save(commit=False)
        response.ocurrence = self.ocurrence
        response.author = self.request.user
        response.save()
        print(response)
        return super().form_valid(form)
    def form_invalid(self, form):
        # Exibe erros de formulário para depuração
        print("Form inválido:", form.errors)
        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('events:response_success')

