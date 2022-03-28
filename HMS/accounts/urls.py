from django.urls import path
from .import views

urlpatterns=[
    path('', views.home, name="home"),
    path('create_patients/',views.createPatient),
    path('patient/<str:pk>/',views.patient),
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout")



]