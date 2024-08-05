# admi_cursos/management/commands/seed_inscripciones.py
from django.core.management.base import BaseCommand
from admi_cursos.models import Inscripciones, Estudiantes, Cursos
from django.utils import timezone


class Command(BaseCommand):
    help = 'Poblar la tabla Inscripciones con datos de prueba'


    def handle(self, *args, **kwargs):
        # Obtener estudiantes
        estudiante1 = Estudiantes.objects.get(usuario='juan_perez')
        estudiante2 = Estudiantes.objects.get(usuario='maria_gomez')
        # Obtener cursos
        curso1 = Cursos.objects.get(nombre='Introducción a Python')
        curso2 = Cursos.objects.get(nombre='Desarrollo Web con Django')


        # Datos para crear o verificar inscripciones
        inscripciones_data = [
            {
                'estudiante': estudiante1,
                'curso': curso1,
                'fecha_inscripcion': timezone.now().date(),
                'estado': 'activo'
            },
            {
                'estudiante': estudiante2,
                'curso': curso2,
                'fecha_inscripcion': timezone.now().date(),
                'estado': 'activo'
            }
        ]


        for inscripcion in inscripciones_data:
            obj, created = Inscripciones.objects.get_or_create(
                estudiante=inscripcion['estudiante'],
                curso=inscripcion['curso'],
                defaults={
                    'fecha_inscripcion': inscripcion['fecha_inscripcion'],
                    'estado': inscripcion['estado']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Inscripción creada con éxito para {inscripcion["estudiante"].usuario}.'))
            else:
                self.stdout.write(self.style.WARNING(f'Inscripción ya existente para {inscripcion["estudiante"].usuario} en el curso {inscripcion["curso"].nombre}.'))