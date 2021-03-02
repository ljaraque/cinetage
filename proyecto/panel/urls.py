from django.urls import path
from . import views

app_name = "panel"

urlpatterns = [
    path('usuarios/', views.ListaUsuarios.as_view(), name='usuarios'),
    path('crear_usuario_cliente/', views.CrearUsuarioCliente.as_view(), name='crear_usuario_cliente'),
    path('crear_usuario_subcliente/', views.CrearUsuarioSubcliente.as_view(), name='crear_usuario_subcliente'),
    path('<pk>/eliminar_usuario/', views.EliminarUsuario.as_view(), name="eliminar_usuario"),
    path('<pk>/editar_usuario_cliente/', views.EditarUsuarioCliente.as_view(), name="editar_usuario_cliente"),
    path('<pk>/editar_usuario_subcliente/', views.EditarUsuarioSubcliente.as_view(), name="editar_usuario_subcliente"),
    path('registro/', views.registro, name='registro'),
]