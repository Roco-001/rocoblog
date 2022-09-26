from django.urls import path
from . import views

#crea tus urls de la app

app_name= 'core'
urlpatterns = [
	path('', views.home, name="home"),

]