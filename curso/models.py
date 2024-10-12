from django.db import models
from persona.models import Persona
from django.core.exceptions import ValidationError

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad_max = models.CharField(max_length=10)
    profesor = models.ForeignKey(Persona, on_delete=models.CASCADE)  
    create_at = models.DateTimeField(auto_now=True)

    estudiantes = models.ManyToManyField(Persona, related_name='cursos_estudiante', blank=True) 
    
    def save(self, *args, **kwargs):
        self.full_clean()  # Valida todo el modelo antes de guardar
        super().save(*args, **kwargs)
    
    def clean(self):
        if self.capacidad_max <= 0:
            raise ValidationError('La capacidad máxima debe ser mayor a 0. ')
        
        if self.profesor.rol != 'profesor':
            raise ValidationError(f'{self.profesor.nombre} {self.profesor.apellidos} no tiene rol de profesor. ')
    
    def __str__(self):
        return f'{self.nombre} - {self.profesor.nombre} - {self.profesor.apellidos} - {self.capacidad_max}'

    class Meta:
        db_table = 'Curso' 