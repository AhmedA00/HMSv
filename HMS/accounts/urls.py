from django.urls import path
from .import views

urlpatterns=[
    path('create_patients/',views.createPatient),
    path('patient/<str:pk>/',views.patient),
    path('register/',views.registerPage),
    path('login/',views.loginPage),
    path('logout/',views.logoutUser)



]