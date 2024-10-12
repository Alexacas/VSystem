from django.contrib import admin
from .models import EstudianteCurso

@admin.register(EstudianteCurso)
class EstudianteCursoAdmin(admin.ModelAdmin):
    list_display = ("id", "estudiante", "curso", "fechaInicio", "fechaFinal", "estado", "notaFinal")
