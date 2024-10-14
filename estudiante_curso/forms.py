from django import forms
from .models import EstudianteCurso

class EstudianteCursoForm(forms.ModelForm):
    class Meta:
        model = EstudianteCurso
        fields = ['estudiante', 'curso', 'fechaInicio', 'fechaFinal', 'estado', 'notaFinal']  