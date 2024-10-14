from django.shortcuts import render, redirect
from .models import EstudianteCurso, Curso
from .forms import EstudianteCursoForm

# Vista para listar los estudiantes y cursos
def Estudiante_Curso(request):
    cursos = Curso.objects.all()

    curso_seleccionado = request.GET.get('curso', 'Todos')  

    if curso_seleccionado == 'Todos':
        estudianteCurso = EstudianteCurso.objects.all()
    else:
        estudianteCurso = EstudianteCurso.objects.filter(curso__nombre=curso_seleccionado)

    return render(request, 'lista_est_cur.html', {
        'title': 'Relación estudiantes y curso',
        'estudiantes_cursos': estudianteCurso,
        'cursos': cursos,  
    })

def formulario_estudiante_curso(request):
    if request.method == 'POST':
        form = EstudianteCursoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('lista-estudiantes-cursos')  
    else:
        form = EstudianteCursoForm()  

    return render(request, 'formulario_estudiante_curso.html', {'form': form})
