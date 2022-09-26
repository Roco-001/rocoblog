from django.urls import path
from . import views

#crea tus urls de la app

app_name= 'about'
urlpatterns = [
	path('', views.about, name="about"),


]