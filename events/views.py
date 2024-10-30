""" Module views for Events """
from datetime import datetime

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import EventOcurrenceForm, EventPatientForm
from .models import ocurrence_models


class EventOcurrenceCreateView(CreateView):
    # pylint:disable=too-many-ancestors
    """Create a event notification."""
    model = ocurrence_models.EventOcurrence
    form_class = EventOcurrenceForm
    template_name = 'events_form.html'
    success_url = reverse_lazy('ocurrence_success')

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
