from django.shortcuts import render, redirect
from .models import Matricula
from .forms import MatriculaForm  

def lista_matriculas(request):
    matriculas = Matricula.objects.all()  
    return render(request, 'lista_matricula.html', {
        'title': 'Lista de Matrículas',
        'matriculas': matriculas,
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
