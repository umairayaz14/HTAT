import imp
from xml.dom.minidom import Document
from django.urls import path
from A_SYST import views
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.init, name="init"),
    path("uploadvideo", views.uploadvideo, name="uploadvideo"),
    path("loginadmin", auth_views.LoginView.as_view(extra_context={ 'next': 'uploadvideo', },), name= "loginadmin"),
    path("logoutadmin", auth_views.LogoutView.as_view(), name="logoutadmin"),
    path("logininstructor", auth_views.LoginView.as_view(extra_context={ 'next': '/instructor', },), name= "logininstructor"),
    path("logoutinstructor", auth_views.LogoutView.as_view(), name="logoutinstructor"),
    path("instructor", views.instructor, name="instructor"),
    path("trainmodel", views.trainmodel, name="trainmodel"),

] 


