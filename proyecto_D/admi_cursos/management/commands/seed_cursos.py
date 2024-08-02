# admi_cursos/management/commands/seed_cursos.py
from django.core.management.base import BaseCommand
from admi_cursos.models import Cursos

class Command(BaseCommand):
    help = 'Poblar la tabla Cursos con datos de prueba'

    def handle(self, *args, **kwargs):
        cursos_data = [
            {
                'nombre': 'Introducción a Python',
                'descripcion': 'Curso básico de Python para principiantes.'
            },
            {
                'nombre': 'Desarrollo Web con Django',
                'descripcion': 'Aprende a construir aplicaciones web robustas con Django.'
            }
        ]

        for curso in cursos_data:
            obj, created = Cursos.objects.get_or_create(
                nombre=curso['nombre'],
                defaults={'descripcion': curso['descripcion']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Curso "{curso["nombre"]}" creado con éxito.'))
            else:
                self.stdout.write(self.style.WARNING(f'Curso "{curso["nombre"]}" ya existe.'))
