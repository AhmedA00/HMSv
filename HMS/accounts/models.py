from django.db import models

# Create your models here.

class Patient (models.Model):
    #Table for the Patients

    name=models.CharField(max_length=200,null=True)
    email=models.EmailField()
    phone=models.CharField(max_length=200,null=True)
    date=models.TimeField()

    def __str__(self):
        # It will show the patient name in the admin
       return self.name

class Doctor (models.Model):
    #Table for the Dr

    SECTION=(
        ('Derma','Derma'),
        ('Dentist','Dentist'),
        ('General','General'),

    )

    name=models.CharField(max_length=200,null=True)
    email=models.EmailField()
    phone=models.CharField(max_length=200,null=True)
    section=models.CharField(max_length=200,null=True,choices=SECTION)
    time_start=models.TimeField('Start of Shift')
    time_end=models.TimeField('End of Shift')

    def __str__(self):
        #It will show the dr name in the admin
       return self.name



class Lab (models.Model):
    TEST=(
        ('CREATINE','CREATINE'),
        ('VITAMINS','VITAMINS'),
        ('PREGNANCY','PREGNANCY'),

    )
    receipt=models.CharField(max_length=200,null=True,choices=TEST)
    patient=models.ForeignKey(Patient,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True,null=True)

class Pharmacy(models.Model):
    PRODUCT=(
        ('PANADOL','PANADOL'),
        ('MULTI-VITAMIN','MULTI-VITAMIN'),
        ('RECCOTAN','RECCOTAN'),
        ('MOUTHWASH','MOUTHWASH'),
    )

    receipt=models.CharField(max_length=200,null=True,choices=PRODUCT)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Appointment(models.Model):

    STATUS=(
        ('Booked','Booked'),
        ('Available','Available'),
        ('Waiting','Waiting')

    )

    patient=models.ForeignKey(Patient,null=True,on_delete=models.SET_NULL)
    doctor=models.ForeignKey(Doctor,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=200,null=True,choices=STATUS)

    def __str__(self):
        #This will show the dr booked with an appointment
       return self.doctor.name