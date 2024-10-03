from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Persona

def get_estudiantes(request):
    
    estudiantes = Persona.objects.filter(rol='Estudiante')
    
    return render(request, 'lista-estudiantes.html',{
        'title': 'Lista de estudiantes ',
        'estudiantes': estudiantes
    })
    
def lista_personas(request):
    personas = Persona.objects.prefetch_related('cursos').filter(rol='estudiante')
    return render(request, 'persona/lista-estudiantes.html', {'personas': personas})


def registrar_persona(request):
        nombre = request.POST.get('txtnombre')
        apellidos = request.POST.get('txtapellido') 
        dni = request.POST.get('numdni')  
        telefono = request.POST.get('numtelefono')
        email = request.POST.get('email')  
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        rol = request.POST.get('txtrol')
        
        peronas = Persona.objects.create(
            nombre = nombre,
            apellidos = apellidos,
            dni = dni,
            telefono = telefono,
            email = email,
            fecha_nacimiento = fecha_nacimiento,
            rol = rol
        )
        
        return redirect('lista-estudiantes')