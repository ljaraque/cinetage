from django.urls import path
from . import views

app_name = "servicio"

urlpatterns = [
    path('', views.principal, name='principal'),

]