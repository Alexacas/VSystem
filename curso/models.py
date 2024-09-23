from django.db import models
from django.db import Persona

class Curso(models.Model):
    id_curso = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    capacidad_max = models.CharField(max_length=10)
    profesor_id = models.ForeignKey(Persona, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)
    

def __str__(self):
    return f'{self.id_curso} - {self.nombre} - {self.capacidad_max} - {self.profesor_id}'
   

class Meta:
    bd_table = 'Curso'