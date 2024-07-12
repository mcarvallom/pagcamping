from django import forms
from django.forms import ModelForm
from .models import Arriendo
from datetime import date
from django.core.exceptions import ValidationError

class RentalForm(ModelForm):
    class Meta:
        model = Arriendo
        fields = ['nombreArriendo', 'apellidoArriendo', 'correoArriendo', 'celularArriendo', 'cant_carpas_menor4', 'cant_carpas_mayor4', 'fecha_inicio_Arriento', 'fecha_fin_Arriendo']
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

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio_Arriento')
        fecha_fin = cleaned_data.get('fecha_fin_Arriendo')
        cant_carpas_menor4 = cleaned_data.get('cant_carpas_menor4')
        cant_carpas_mayor4 = cleaned_data.get('cant_carpas_mayor4')

        if fecha_inicio and fecha_fin:
            if fecha_inicio >= fecha_fin:
                raise ValidationError("La fecha de inicio debe ser anterior a la fecha de término.")
        
        if cant_carpas_menor4 == 0 and cant_carpas_mayor4 == 0:
            raise ValidationError("Debe arrendar al menos un tipo de carpa (hasta 4 personas o sobre 4 personas).")

        return cleaned_data