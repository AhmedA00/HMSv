from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),

    path('create_appointments/', views.createAppointment, name="create_appointment"),
    path('update_appointments/<str:pk>/', views.updateAppointment, name="update_appointments"),

    path('patient/<str:pk>/', views.patient, name="patient"),
    path('doctor/',views.doctor,name="doctor"),
    path('doctor_form/<str:pk>/',views.updateDoctor,name="doctor_form"),

    path('lab/',views.lab),

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/',views.userPage,name="user-page")



]