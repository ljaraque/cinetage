from django.urls import path
from . import views

app_name = "servicio"

urlpatterns = [
    path('', views.principal, name='principal'),
    path('lista_peliculas/', views.ListaPeliculas.as_view(), name='lista_peliculas'),
    path('<pk>', views.DetallePelicula.as_view(), name='detalle_pelicula')

]