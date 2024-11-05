""" Module views for Events """
from datetime import datetime

from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from events.forms.event_ocurrence_forms import EventOcurrenceForm
from events.forms.event_patient_forms import EventPatientForm
from events.models.event_ocurrence_models import EventOcurrence


class EventOcurrenceCreateView(CreateView):
    # pylint:disable=too-many-ancestors
    """Create a event notification."""
    model = EventOcurrence
    form_class = EventOcurrenceForm
    template_name = 'event/events_form.html'
    success_url = reverse_lazy('event_success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient_form'] = EventPatientForm(self.request.POST or None)
        context['current_date'] = datetime.now()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        patient_form = context['patient_form']
        if form.cleaned_data.get('patient_involved'):
            if patient_form.is_valid():
                patient = patient_form.save()
                form.instance.patient = patient
            else:
                return self.form_invalid(form)

        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get_success_url(self) -> str:
        return reverse('event_success', kwargs={'pk': self.object.id})


class EventSucessTemplateView(TemplateView):
    """Page Sucess Event Send"""
    template_name = "event/event_sucess.html"

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        event = get_object_or_404(EventOcurrence, pk=self.kwargs.get('pk'))
        context['event'] = event
        # context['pk'] = self.kwargs.get('pk')
        return context
