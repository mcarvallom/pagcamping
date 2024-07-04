from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contacto
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password1','password2']

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = ['nombreContacto', 'correoArriendo', 'mensaje']
        widgets={
            'nombreContacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'id': 'nombren'}),
            'correoArriendo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico', 'id': 'correon'}),
            'mensaje': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mensaje', 'id': 'mensajen'})
        }
