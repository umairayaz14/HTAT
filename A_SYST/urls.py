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
    path("login", auth_views.LoginView.as_view(), name= "login"),


] 


