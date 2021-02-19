from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=25)
    ultima_actualizacion = models.DateTimeField(auto_now=True)


class Actor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ultima_actualizacion = models.DateTimeField(auto_now=True)


class Idioma(models.Model):
    nombre = models.CharField(max_length=50)
    ultima_actualizacion = models.DateTimeField(auto_now=True)


class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    agno_publicacion = models.IntegerField()
    duracion_arriendo = models.IntegerField()
    precio_arriendo = models.DecimalField(max_digits=4, decimal_places=2, default=4.99)
    largo = models.IntegerField()
    costo_reemplazo = models.DecimalField(max_digits=5, decimal_places=2, default=19.99)
    clasificacion = models.CharField(max_length=25)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    actores = models.ManyToManyField(Actor)
    #special_features Omitido
    #full_text Omitido


class Inventario(models.Model):
    id_tienda = models.IntegerField()
    peliculas = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    ultima_actualizacion = models.DateTimeField(auto_now=True)


class Arriendo(models.Model):
    fecha_arriendo = models.DateTimeField()
    inventario = models.ForeignKey(Inventario, default=1, on_delete=models.DO_NOTHING)
    temporal = models.IntegerField()
    id_cliente = models.IntegerField()
    fecha_devolucion = models.DateTimeField(null=True)
    id_empleado = models.IntegerField()
    ultima_actualizacion = models.DateTimeField(auto_now=True)
