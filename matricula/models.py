from django.db import models
from estudiante_curso.models import EstudianteCurso

class Matricula(models.Model):
    estado = models.CharField(max_length=150) 
    fecha_inicio = models.DateField() 
    costo = models.DecimalField(max_digits=8, decimal_places=1)
    estudiante_curso = models.ForeignKey(EstudianteCurso, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Matrícula de {self.estudiante_curso.estudiante.nombre} en {self.estudiante_curso.curso.nombre} - Estado: {self.estado} - Costo: {self.costo}'

    class Meta:
        db_table = 'Matriculas'  # Cambié a plural para seguir la convención
