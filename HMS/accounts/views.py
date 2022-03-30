from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

from .forms import AppointmentForm, CreateUserForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def registerPage(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')  # To get the username created
                messages.success(request, 'Account was created for ' + user)  # Message to pop up when registered

                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    # Login function to get in the system
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            # Making sure that the user is registered and correct
            if user is not None:
                login(request, user)
                return redirect('home')
                # If the information was incorrect a message will show that
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    # Logout function that redirects the user to the login page
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    appointments = Appointment.objects.all()
    patients = Patient.objects.all()

    total_patients = patients.count()

    total_appointments = Appointment.objects.all().count()

    pending = appointments.filter(status='Waiting').count()

    context = {'appointments': appointments, 'patients': patients,
               'total_appointments': total_appointments, 'pending': pending}

    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
def patient(request, pk):
    patient = Patient.objects.get(id=pk)
    appointments = patient.appointment_set.all()
    appointment_count = appointments.count

    context = {'patient': patient, 'appointments': appointments,
               'appointment_count': appointment_count}
    return render(request, 'accounts/patient.html', context)

@login_required(login_url='login')
def doctor(request):
    # doctor = Doctor.objects.get(id=pk)
    doctor = Doctor.objects.all()

    # appointments = Appointment.objects.filter(doctor=doctor)
    # appointment_count = appointments.count

    # context = {'doctor': doctor, 'appointments': appointments,
    #            'appointment_count': appointment_count},
    context = {'doctor': doctor}
    return render(request, 'accounts/doctor.html', context)

@login_required(login_url='login')
def updateDoctor(request, pk):
    doctor = Doctor.objects.get(id=pk)

    appointments = Appointment.objects.filter(doctor=doctor)
    appointment_count = appointments.count

    context = {'doctor': doctor, 'appointments': appointments,
               'appointment_count': appointment_count}

    return render(request, 'accounts/doctor_form.html', context)



@login_required(login_url='login')
def createAppointment(request):
    # To render the appointment form and edit on it
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/appointment_form.html', context)

@login_required(login_url='login')
def updateAppointment(request, pk):
    form = AppointmentForm()
    context = {'form': form}
    return render(request, 'accounts/appointment_form.html', context)
