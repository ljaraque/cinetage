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
    #special_features Omitido
    #full_text Omitido
    
    #related
    idioma = models.ForeignKey(Idioma, null=True, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    actores = models.ManyToManyField(Actor)

    #temp
    temporal_idioma = models.IntegerField()



class Inventario(models.Model):
    id_tienda = models.IntegerField()
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    
    #related
    pelicula = models.ForeignKey(Pelicula, null=True, on_delete=models.CASCADE)

    #temp
    temporal_pelicula= models.IntegerField()


class Arriendo(models.Model):
    fecha_arriendo = models.DateTimeField()
    id_cliente = models.IntegerField()
    fecha_devolucion = models.DateTimeField(null=True)
    id_empleado = models.IntegerField()
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    #related
    inventario = models.ForeignKey(Inventario, null=True, on_delete=models.CASCADE)

    #temp
    temporal_inventario = models.IntegerField()