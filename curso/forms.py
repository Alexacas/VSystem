from django import forms
from .models import curso  # Asegúrate de que el modelo está importado

class CursoForm(forms.ModelForm):
    class Meta:
        model = curso
        fields = ['nombre', 'capacidad_max', 'profesor']  # Los campos del curso que serán editables
