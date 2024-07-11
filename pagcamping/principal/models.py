from django.db import models
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.exceptions import ValidationError

# Create your models here.
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  # Campos que quieres editar

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Actualizar'))
class Cliente (models.Model):
    run         = models.CharField(max_length=10)
    dv          = models.CharField(max_length=1)
    nombre      = models.CharField(max_length= 60)
    apellido    = models.CharField(max_length= 60)
    correo      = models.EmailField(unique=True, max_length=80, blank=True, null=True )
    celular     = models.CharField(max_length=10)
    direccion   = models.CharField(max_length= 120)
    def __str__(self):
        return str(self.nombre)+ " " +str(self.correo)
 
class Arriendo (models.Model):
    idArriendo     = models.CharField(primary_key=True, max_length=10)
    nombreArriendo  = models.CharField(max_length=60) 
    apellidoArriendo    = models.CharField(max_length= 60)
    correoArriendo      = models.EmailField(max_length=80)
    celularArriendo     = models.CharField(max_length=10)
    cant_carpas_menor4  = models.IntegerField(default=1)
    cant_carpas_mayor4  = models.IntegerField(default=0)
    fecha_inicio_Arriento = models.DateField(null=False)
    fecha_fin_Arriendo    = models.DateField(null=False)

    def clean(self):
        if self.fecha_inicio_Arriento >= self.fecha_fin_Arriendo:
            raise ValidationError("La fecha de inicio debe ser anterior a la fecha de término.")
 
class Contacto (models.Model):
    idContacto   = models.IntegerField(primary_key=True)
    nombreContacto = models.CharField(max_length=60)
    correoArriendo      = models.EmailField( max_length=80, blank=False, null=False )
    mensaje      = models.CharField(max_length=255)

    def __str__(self):
        return str(self.nombreContacto) + " " + str(self.mensaje)


class Categoria (models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombreCategoria = models.CharField(max_length=60)

    def __str__(self):
        return str(self.nombreCategoria)

    class Meta:
        db_table = 'Categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['idCategoria']

class Producto (models.Model):
    id = models.IntegerField(primary_key=True)
    nombreProducto = models.CharField(max_length=60)
    detalle        = models.CharField(max_length=200)
    image          = models.CharField(max_length=250, blank=True)
    precio          = models.IntegerField(default=0)
    cantidad       = models.IntegerField(default=0)
    disponible     = models.BooleanField(default=True)
    categoria      = models.ForeignKey(Categoria, null= True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombreProducto)+ " " + str(self.precio) + " " + str(self.cantidad)

    class Meta:
        db_table = 'Producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']