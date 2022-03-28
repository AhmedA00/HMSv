from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

from .forms import PatientForm

# Create your views here.


def patient (request,pk):
    patient=Patient.objects.get(id=pk)
    appointments=patient.order_set.all()
    appointment_count=appointments.count

    context={'patient':patient,'appointments':appointments,
             'appointment_count':appointment_count}
    return render(request,'accounts/patient.html',context)


def createPatient (request):
# To render the patient form and edit on it
    form=PatientForm()

    context={'form':form}
    return render(request,'accounts/patient_form',context)
