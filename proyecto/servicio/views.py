from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Pelicula, Categoria


# cliente o subcliente
def usuario_permitido2(usuario):
    if usuario.rol == "cliente" or usuario.rol == "subcliente":
        validacion = True
    else:
        validacion = False
    return validacion

# Create your views here.

def principal(request):
    return render(request, 'servicio/principal.html')


# Lista de Películas

class ListaPeliculas(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Pelicula
    context_object_name = 'lista_por_categorias'
    #extra_context = {'mensaje_especial':'ListView menos automatizada '}
    template_name = 'servicio/lista_peliculas.html'

    def get_queryset(self):
        categorias=Categoria.objects.all()
        categorias_nombres = []
        for categoria in categorias:
            categorias_nombres.append(categoria.nombre)
        print(categorias_nombres)
        peliculas_por_categorias=[]
        for categoria in categorias_nombres:
            peliculas=Pelicula.objects.all()[:300]
            peliculas_categoria = []
            for pelicula in peliculas:
                if len(peliculas_categoria)>=4:
                    break
                if categoria == pelicula.categorias.all()[0].nombre:
                    peliculas_categoria.append(pelicula)
            peliculas_por_categorias.append({'nombre_categoria': categoria, 
                                            'peliculas': peliculas_categoria})
        queryset = peliculas_por_categorias
        return queryset

    def test_func(self):
        return usuario_permitido2(self.request.user)

# Detalle Pelicula

class DetallePelicula(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Pelicula
    context_object_name = 'detalle_pelicula'
    template_name = 'servicio/detalle_pelicula.html'

    def test_func(self):
        return usuario_permitido2(self.request.user)