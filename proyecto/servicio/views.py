from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Pelicula, Categoria
from django.urls import reverse_lazy


# cliente o subcliente
def usuario_permitido2(usuario):
    if usuario.rol == "cliente" or usuario.rol == "subcliente":
        validacion = True
    else:
        validacion = False
    return validacion

# Create your views here.

def principal(request):
    context=dict()
    if 'num_visitas' not in request.session:
        request.session['num_visitas']= 1
    else:
        request.session['num_visitas'] += 1
    context['num_visitas']=request.session['num_visitas']
    return render(request, 'servicio/principal.html', context)


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


# CRUD Películas

# C de CRUD
class CrearPelicula(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Pelicula
    fields = ['titulo','descripcion','agno_publicacion','largo','clasificacion',
                'idioma','categorias', 'actores']
    template_name = 'servicio/crear_pelicula.html'
    success_url = reverse_lazy('servicio:peliculas')

    def test_func(self):
        return self.request.user.rol=="operador"

# R de CRUD
class PeliculasCV(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Pelicula
    context_object_name = 'peliculas'
    template_name = 'servicio/peliculas.html'

    def test_func(self):
        return self.request.user.rol=="operador"
'''
class Peliculas(LoginRequiredMixin, UserPassesTestMixin, View):
    model = Pelicula
    template_name = 'servicio/peliculas.html'
    def get(self, request):
        print("hola")
        context = {'peliculas':Pelicula.objects.all().order_by('id')}
        return render(request, 'servicio/peliculas.html', context)
'''

# U de CRUD
class EditarPelicula(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pelicula
    fields = ['titulo','descripcion','agno_publicacion','largo','clasificacion',
                'idioma','categorias', 'actores']
    template_name = 'servicio/editar_pelicula.html'
    success_url = reverse_lazy('servicio:peliculas')

    def test_func(self):
        return self.request.user.rol=="operador"

# D de CRUD
class EliminarPelicula(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pelicula
    template_name = 'servicio/eliminar_pelicula.html'
    success_url = reverse_lazy('servicio:peliculas')

    def test_func(self):
        return self.request.user.rol=="operador"