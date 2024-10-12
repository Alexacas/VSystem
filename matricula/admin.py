from django.contrib import admin
from .models import Matricula

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ("id", "estado", "fecha_inicio", "costo", "estudiante_curso")