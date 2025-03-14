from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['name', 'age', 'hc']
        labels = {
            'name': 'Nombre',
            'age': 'Edad',
            'hc': 'Historia Clinica',
        }