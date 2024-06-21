from django.db import models


# Create your models here.

class Cliente (models.Model):
    username    = models.CharField(max_length= 60)
    run         = models.CharField(primary_key=True, max_length=10)
    dv          = models.CharField(max_length=1)
    nombre      = models.CharField(max_length= 60)
    apellido    = models.CharField(max_length= 60)
    correo      = models.EmailField(unique=True, max_length=80, blank=True, null=True )
    celular     = models.CharField(max_length=10)
    direccion   = models.CharField(max_length= 120)

class Arriendo (models.Model):
    idArriendo     = models.CharField(primary_key=True, max_length=10)
    nombreArriendo  = models.CharField(max_length=60) 
    apellidoArriendo    = models.CharField(max_length= 60)
    correoArriendo      = models.EmailField( max_length=80, blank=True, null=True )
    celularArriendo     = models.CharField(max_length=10)
    cant_carpas_menor4  = models.IntegerField(max_length=2)
    cant_carpas_mayor4  = models.IntegerField(max_length=2)
    fecha_inicio_Arriento = models.DateField(null=False)
    fecha_fin_Arriendo    = models.DateField(null=False)
    
class Producto (models.Model):
    idProducto = models.IntegerField(primary_key=True, max_length=10)
    nombreProducto = models.CharField(max_length=60)
    detalle        = models.CharField(max_length=200)
    valor          = models.IntegerField(max_length=10)
    cantidad       = models.IntegerField(max_length=10)


class Contacto (models.Model):
    idContacto   = models.IntegerField(primary_key=True, max_length=10)
    nombreContacto = models.CharField(max_length=60)
    correoArriendo      = models.EmailField( max_length=80, blank=True, null=True )
    mensaje      = models.CharField(max_length=255)

