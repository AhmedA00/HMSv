from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),

    path('delete_appointment/<str:pk>/',views.deleteAppointment,name="delete_appointment"),
    path('create_appointments/<str:pk>/', views.createAppointment, name="create_appointments"),
    path('update_appointments/<str:pk>/', views.updateAppointment, name="update_appointments"),

    path('patientHome/' ,views.patientHome,name="patientHome"),
    path('patient/<str:pk>/', views.patient, name="patient"),
    path('doctor/',views.doctor,name="doctor"),
    path('doctor_form/<str:pk>/',views.updateDoctor,name="doctor_form"),

    path('lab/',views.lab,name="lab"),
    path('lab_form',views.createLab,name="lab_form"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/',views.userPage,name="user-page")



]