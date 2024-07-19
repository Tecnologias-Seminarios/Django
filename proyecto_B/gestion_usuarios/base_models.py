#gestion_usuarios/base_models.py
from django.db import models


class Persona(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

    class Meta:
        abstract = True