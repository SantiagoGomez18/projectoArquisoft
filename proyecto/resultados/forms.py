from django import forms
from .models import Resultado

class ResultadoForm(forms.ModelForm):
    class Meta:
        model = Resultado
        fields = ['paciente', 'fecha', 'resultado']
        labels = {
            'paciente': 'Paciente',
            'fecha': 'Fecha',
            'resultado': 'Resultado',
        }
        