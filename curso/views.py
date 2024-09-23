from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Persona

def get_curso(request):
    
    profesor = Persona.objects.filter(rol='Profesor')
    
    return render(request, 'lista-curso.html',{
        'title': 'Lista curso ',
        'profesores': profesor
    })

