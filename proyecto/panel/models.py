from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

'''
class Usuario(AbstractUser):
    ROLES = (
        ("operador", "Operador"),
        ("cliente", "Cliente"),
        ("subcliente", "Subcliente"),
    )
    rol = models.CharField(max_length=50, choices=ROLES)
    descripcion = models.TextField
'''