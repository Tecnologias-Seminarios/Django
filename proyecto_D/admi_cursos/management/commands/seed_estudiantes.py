# admi_cursos/management/commands/seed_estudiantes.py
from django.core.management.base import BaseCommand
from admi_cursos.models import Estudiantes
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Poblar la tabla Estudiantes con datos de prueba'

    def handle(self, *args, **kwargs):
        estudiantes_data = [
            {
                'usuario': 'juan_perez',
                'nombre': 'Juan',
                'apellidos': 'Perez',
                'edad': 30,
                'fecha_nacimiento': '1990-01-01',
                'contrasena': 'contraseña123'
            },
            {
                'usuario': 'maria_gomez',
                'nombre': 'Maria',
                'apellidos': 'Gomez',
                'edad': 28,
                'fecha_nacimiento': '1992-02-02',
                'contrasena': 'contraseña456'
            }
        ]

        for estudiante in estudiantes_data:
            obj, created = Estudiantes.objects.get_or_create(
                usuario=estudiante['usuario'],
                defaults={
                    'nombre': estudiante['nombre'],
                    'apellidos': estudiante['apellidos'],
                    'edad': estudiante['edad'],
                    'fecha_nacimiento': estudiante['fecha_nacimiento'],
                    'contrasena': make_password(estudiante['contrasena'])
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Usuario {estudiante["usuario"]} creado con éxito.'))
            else:
                self.stdout.write(self.style.WARNING(f'Usuario {estudiante["usuario"]} ya existe.'))


