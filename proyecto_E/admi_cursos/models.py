#admi_cursos/models.py
from django.db import models
from django.contrib.auth.hashers import make_password
from .base_models import Persona
# Create your models here.
class Estudiantes(Persona):
    usuario = models.CharField(max_length=50, unique=True)
    contrasena = models.CharField(max_length=255)




    def save(self, *args, **kwargs):
        # Encriptar la contraseña antes de guardarla
        self.contrasena = make_password(self.contrasena)
        super(Estudiantes, self).save(*args, **kwargs)




    def __str__(self):
        return "Soy el estudiante: {} y tengo {} años".format(self.nombre, self.edad)
    
class Cursos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()


    def __str__(self):
        return self.nombre

# Modelo Inscripciones en admi_cursos/models.py
class Inscripciones(models.Model):
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()
    estado = models.CharField(max_length=10, choices=[('activo', 'Activo'), ('completado', 'Completado'), ('cancelado', 'Cancelado'), ('en espera', 'En espera')], default='activo')


    def __str__(self):
        return f"{self.estudiante.nombre} inscrito en {self.curso.nombre} el {self.fecha_inscripcion}"