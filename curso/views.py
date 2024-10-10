from django.shortcuts import render
<<<<<<< HEAD
from .models import Curso
from persona.models import Persona

def get_cursos(request):
    
    cursos = Curso.objects.all() 
    profesor = Persona.objects.filter(rol='Profesor')  
    return render(request, 'lista-curso.html', {
        'title': 'Lista de cursos',
        'cursos': cursos
        })
    
    ## falta filtrar profesor, cursos funcionando
=======

# Create your views here.
>>>>>>> 3f6871f1d622b82cb8675ec113f60789721c189a
