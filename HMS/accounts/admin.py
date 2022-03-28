from django.contrib import admin
from .models import Patient,Doctor,Appointment,Lab,Pharmacy

# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Pharmacy)
admin.site.register(Lab)