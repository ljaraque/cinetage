from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    ROLES = ( 
        ("superadmin", "Superadmin  "), 
        ("operador", "Operador"), 
        ("cliente", "Cliente"), 
        ("subcliente", "Subcliente"), 
    ) 
    apellido_paterno = models.CharField(max_length=50, null=True, verbose_name="Apellido Paterno")
    apellido_materno = models.CharField(max_length=50, null=True, verbose_name="Apellido Materno")
    rol = models.CharField(max_length=50, choices=ROLES)
    principal = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
