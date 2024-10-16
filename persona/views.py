from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm

def get_estudiantes(request):
    
    estudiantes = Persona.objects.filter(rol='Estudiante')
    
    return render(request, 'lista-estudiantes.html',{
        'title': 'Lista de estudiantes ',
        'estudiantes': estudiantes
    })

# Vista para agregar nuevos estudiantes
def formulario_estudiante(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            estudiante = form.save(commit=False)  
            estudiante.rol = 'Estudiante'  
            estudiante.save()  
            return redirect('lista-estudiantes')  
    else:
        form = PersonaForm()

    return render(request, 'formulario_estudiante.html', {'form': form})
