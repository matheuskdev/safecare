from typing import Any
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from events.models.response_ocurrence_models import ResponseOcurrence
from events.models.event_ocurrence_models import EventOcurrence


class EventResponseOcurrenceCreateView(CreateView):
    """Create a response for an occurrence"""
    model = ResponseOcurrence
    form_class = 'EventResponseOcurrenceForm'
    template_name = 'response/events_form.html'
    success_url = reverse_lazy('response_success')

    def dispatch(self, request, *args, **kwargs):
        # Recupera a ocorrência antes de criar a resposta
        self.ocurrence = get_object_or_404(
            EventOcurrence, id=kwargs['ocurrence_id']
        )
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Associa a resposta com a ocorrência recuperada
        form.instance.ocurrence = self.ocurrence
        return super().form_valid(form)
