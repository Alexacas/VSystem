from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellidos', 'dni', 'telefono', 'email', 'fecha_nacimiento']  # Elimina 'rol' de los campos editables
