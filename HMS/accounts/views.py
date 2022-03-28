from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

from .forms import PatientForm, CreateUserForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout

# Create your views here.

def registerPage(request):
    form= CreateUserForm()

    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')#To get the username created
            messages.success(request,'Account was created for '+ user)#Message to pop up when registered

            return redirect('login')

    context={'form':form}
    return render(request,'accounts/register.html',context)

def loginPage(request):
#Login function to get in the system
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

            #Making sure that the user is registered and correct
        if user is not None:
            login(request,user)
            return redirect('home')
            #If the information was incorrect a message will show that
        else:
            messages.info(request,'Username or Password is incorrect')

    context={}
    return render(request,'accounts/login.html',context)

def logoutUser (request):
#Logout function that redirects the user to the login page
    logout(request)
    return redirect('login')


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
