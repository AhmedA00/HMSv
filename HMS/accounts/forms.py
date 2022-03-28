from django.forms import ModelForm


from .models import Appointment

class PatientForm (ModelForm):
    class Meta :
        model= Appointment
        fields='__all__'

