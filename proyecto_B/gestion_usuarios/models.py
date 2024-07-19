#gestion_usuarios/models.py
from django.db import models
from django.contrib.auth.hashers import make_password
from .base_models import Persona


# Create your models here.
class Usuario(Persona):
    usuario = models.CharField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=255)


    def save(self, *args, **kwargs):
        # Encriptar la contraseña antes de guardarla
        self.contraseña = make_password(self.contraseña)
        super(Usuario, self).save(*args, **kwargs)


    def __str__(self):
        return "Hola mi nombre es: {} y tengo {} años".format(self.nombre, self.edad)