from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#from .models import Usuario
User = get_user_model()


# funciones test_func

# operador o cliente
def usuario_permitido_operador_cliente(usuario):
    if usuario.rol == "operador" or usuario.rol == "cliente":
        validacion = True
    else:
        validacion = False
    return validacion

# operador
def usuario_permitido_operador(usuario):
    if usuario.rol == "operador":
        validacion = True
    else:
        validacion = False
    return validacion


# Create your views here.


###############################################################################
# C de CRUD
###############################################################################

# C de CRUD Usuario con rol="cliente"
from .forms import FormularioCrearUserCliente
from django.contrib.auth.forms import UserCreationForm


class CrearUsuarioCliente(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = User
    form_class = FormularioCrearUserCliente
    success_url = reverse_lazy('panel:usuarios')
    template_name = 'panel/usuario_crear_cliente.html'

    def form_valid(self, form):
        form.instance.rol = "cliente"
        return super(CrearUsuarioCliente, self).form_valid(form)

    def test_func(self):
        return usuario_permitido_operador(self.request.user)


# C de CRUD Usuario con rol="subcliente"
from .forms import FormularioCrearUserSubcliente
class CrearUsuarioSubcliente(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = User
    form_class = FormularioCrearUserSubcliente
    success_url = reverse_lazy('panel:usuarios')
    template_name = 'panel/usuario_crear_subcliente.html'

    def get_form(self, form_class=None):
        form = super().get_form(FormularioCrearUserSubcliente)
        if self.request.user.rol=="operador":
            form.fields['principal'].queryset = User.objects.filter(rol="cliente").order_by("username")
        elif self.request.user.rol=="cliente":
            form.fields.pop("principal")
        return form

    def form_valid(self, form):
        user = self.request.user
        form.instance.rol = "subcliente"
        if user.rol=="cliente":
            form.instance.principal = user
        return super(CrearUsuarioSubcliente, self).form_valid(form)

    def test_func(self):
        return usuario_permitido_operador_cliente(self.request.user)


###############################################################################
# R de CRUD
###############################################################################

class ListaUsuarios(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    #queryset = User.objects.filter(profile__rol__in=["cliente", "subcliente"]).order_by("id")
    context_object_name = 'usuarios'
    template_name = 'panel/usuarios.html'

    def test_func(self):
        return usuario_permitido_operador_cliente(self.request.user)

    def get_queryset(self):
        if self.request.user.rol == "operador":
            return User.objects.filter(rol__in=["cliente", "subcliente"]).order_by("id")
        if self.request.user.rol == "cliente":
            return User.objects.filter(principal=self.request.user).order_by("id")


###############################################################################
# U de CRUD
###############################################################################

# U de CRUD Usuario con rol="cliente"
from .forms import FormularioEditarUserCliente
class EditarUsuarioCliente(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = FormularioEditarUserCliente
    success_url = reverse_lazy('panel:usuarios')
    template_name = 'panel/usuario_crear_cliente.html'

    def form_valid(self, form):
        form.instance.rol = "cliente"
        return super(EditarUsuarioCliente, self).form_valid(form)

    def test_func(self):
        return usuario_permitido_operador(self.request.user)


# U de CRUD Usuario con rol="subcliente"
from .forms import FormularioEditarUserSubcliente
class EditarUsuarioSubcliente(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = FormularioEditarUserSubcliente
    success_url = reverse_lazy('panel:usuarios')
    template_name = 'panel/usuario_crear_subcliente.html'

    def get_form(self, form_class=None):
        form = super().get_form(FormularioEditarUserSubcliente)
        if self.request.user.rol=="operador":
            form.fields['principal'].queryset = User.objects.filter(rol="cliente").order_by("username")
        elif self.request.user.rol=="cliente":
            form.fields.pop("principal")
        return form

    def form_valid(self, form):
        user = self.request.user
        form.instance.rol = "subcliente"
        if user.rol=="cliente":
            form.instance.principal = user
        return super(EditarUsuarioSubcliente, self).form_valid(form)

    def test_func(self):
        return usuario_permitido_operador_cliente(self.request.user)


###############################################################################
# D de CRUD
###############################################################################

class EliminarUsuario(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    context_object_name = 'usuario'
    template_name = 'panel/usuario_confirma_eliminar.html'
    success_url = reverse_lazy('panel:usuarios')

    def test_func(self):
        # ojo este permiso debe implementar que usuario cliente pueda
        # borrar solo subclientes que le pertenecen
        return usuario_permitido_operador_cliente(self.request.user)


###############################################################################
# Registro de Usuario
###############################################################################
#from django.contrib.auth import login, authenticate
from .forms import FormularioRegistroUser
def registro(request):
    if request.method == 'POST':
        form = FormularioRegistroUser(request.POST)
        if form.is_valid():
            #form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            User.objects.create_user(username=username, password=raw_password, rol="cliente")
            #user = authenticate(username=username, password=raw_password, rol="subcliente")
            #login(request, user)
            return redirect('servicio:principal')
    else:
        form = FormularioRegistroUser()
    return render(request, 'panel/usuario_registro.html', {'form': form})


'''
def registro(request):

    if request.method == 'GET':
        form = FormularioRegistroUser()
        return render(request, 'panel/usuario_registro.html', {'form':form})

    if request.method == 'POST':
        form = FormularioRegistroUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            User.objects.create_user(username=username,
                                    password=password,
                                    first_name=first_name,
                                    last_name=last_name)
            return redirect('servicio:principal')
'''            


