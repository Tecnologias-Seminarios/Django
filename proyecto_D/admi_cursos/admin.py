# admi_cursos/admin.py
from django.contrib import admin
from .models import Estudiantes,Cursos,Inscripciones
# Register your models here.


@admin.register(Estudiantes)
class EstudiantesAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nombre', 'apellidos', 'edad', 'fecha_nacimiento')
    search_fields = ('usuario', 'nombre', 'apellidos')

@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')  
    search_fields = ('nombre',)

@admin.register(Inscripciones)
class InscripcionesAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'curso', 'fecha_inscripcion', 'estado')
    search_fields = ('estudiante__usuario', 'curso__nombre') 
    list_filter = ('estado', 'fecha_inscripcion')