from datetime import datetime

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import EventOcurrenceForm, EventPatientForm
from .models import EventOcurrence, EventPatient


class EventOcurrenceCreateView(CreateView):
    model = EventOcurrence
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
        print(f"PATIENT FORM VALID:")
        # Verifica se há um paciente envolvido
        if form.cleaned_data.get('patient_involved'):
            print("PRIMEIRO IF")
            # Verifica se o formulário do paciente é válido
            if patient_form.is_valid():
                print("SEGUNDO IF")
                patient = patient_form.save()  
                form.instance.patient = patient
                print("PASSEI AQUI SALVO **********************************************************")
                print(patient_form)
            else:
                return self.form_invalid(form)

        return super().form_valid(form)
    
    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        print("deu merda **********************************************************")
        print(context)
        return self.render_to_response(context)
