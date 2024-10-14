from django.shortcuts import render, redirect
from .models import Matricula
from .forms import MatriculaForm 
from estudiante_curso.models import Curso 

def lista_matriculas(request):
    cursos = Curso.objects.all()  
    curso_filtrado = request.GET.get('curso')  
    if curso_filtrado:
        matriculas = Matricula.objects.filter(estudiante_curso__curso__nombre=curso_filtrado)
    else:
        matriculas = Matricula.objects.all()

    return render(request, 'lista_matricula.html', {
        'title': 'Lista de Matrículas',
        'matriculas': matriculas,
        'cursos': cursos,  
        'curso_filtrado': curso_filtrado  
    })
    
    

# Vista para agregar o editar una matrícula
def formulario_matricula(request):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('lista-matriculas')  
    else:
        form = MatriculaForm()  

    return render(request, 'formulario_matricula.html', {'form': form})
