from django.db import models

# Create your models here.
class Curso(models.Model):
    
    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.nombre} - {self.camada}'
    
    class Meta():
        verbose_name = 'Course'
    
class Estudiante(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    
class Profesor(models.Model):
    
    nombre = models.CharField(max_length=38)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    
class Entregable(models.Model):
    
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()