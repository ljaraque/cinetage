from django.urls import path
from . import views

app_name = "servicio"

urlpatterns = [
    path('', views.principal, name='principal'),
    path('lista_peliculas/', views.ListaPeliculas.as_view(), name='lista_peliculas'),
    path('peliculas/', views.PeliculasCV.as_view(), name='peliculas'),
    path('crear_pelicula/', views.CrearPelicula.as_view(), name='crear_pelicula'),
    path('<pk>/eliminar_pelicula/', views.EliminarPelicula.as_view(), name='eliminar_pelicula'),
    path('<pk>/editar_pelicula/', views.EditarPelicula.as_view(), name='editar_pelicula'),
    path('<pk>', views.DetallePelicula.as_view(), name='detalle_pelicula')

]