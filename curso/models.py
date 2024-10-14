from django.db import models
from persona.models import Persona
from django.core.exceptions import ValidationError

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad_max = models.IntegerField()
    profesor = models.ForeignKey(Persona, limit_choices_to={'rol': 'profesor'},on_delete=models.CASCADE)  
    create_at = models.DateTimeField(auto_now=True)

    estudiantes = models.ManyToManyField(Persona, related_name='cursos_estudiante', blank=True) 
    
    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)
    
    def clean(self):
        try:
            self.capacidad_max = int(self.capacidad_max)  
        except ValueError:
            raise ValidationError("Capacidad máxima debe ser un número entero.")
        
        if self.capacidad_max <= 0:
            raise ValidationError("Capacidad máxima debe ser mayor que 0.")
        
        if self.profesor.rol != 'profesor':
            raise ValidationError(f'{self.profesor.nombre} {self.profesor.apellidos} no tiene rol de profesor. ')
    
    def __str__(self):
        return f'{self.nombre} - {self.profesor.nombre} - {self.profesor.apellidos} - {self.capacidad_max}'

    class Meta:
        db_table = 'Curso' 