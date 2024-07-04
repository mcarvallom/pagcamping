from django import forms
from django.forms import ModelForm
from .models import Arriendo
from datetime import date

class RentalForm(ModelForm):
    class Meta:
        model = Arriendo
        fields = ['nombreArriendo', 'apellidoArriendo', 'correoArriendo', 'celularArriendo', 'cant_carpas_menor4', 'cant_carpas_mayor4', 'fecha_inicio_Arriento',  'fecha_fin_Arriendo']
        widgets = {
            'nombreArriendo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'id': 'inputName'}),
            'apellidoArriendo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos', 'id': 'inputApellido'}),
            'correoArriendo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@gmail.com', 'id': 'inputEmail4'}),
            'celularArriendo': forms.NumberInput(attrs={'class': 'form-control', 'id': 'inputCelular'}),
            'cant_carpas_menor4': forms.NumberInput(attrs={'class': 'form-control', 'id': 'inputCarpaHastaCuatro', 'min': '0', 'max': '10'}),
            'cant_carpas_mayor4': forms.NumberInput(attrs={'class': 'form-control', 'id': 'inputSobreCuatro', 'min': '0', 'max': '10'}),
            'fecha_inicio_Arriento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'inicioFecha', 'min': date.today().strftime('%Y-%m-%d'), 'max': '2025-12-31'}),
            'fecha_fin_Arriendo': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'finFecha', 'min' : date.today().strftime('%Y-%m-%d')})
        }

   
 
      