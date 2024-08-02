# admi_cursos/management/commands/seed_all.py
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import transaction


class Command(BaseCommand):
    help = 'Ejecuta todos los seeders para poblar la base de datos'


    def handle(self, *args, **kwargs):
        with transaction.atomic():
            try: 
                self.stdout.write(self.style.SUCCESS('Ejecutando seeders...'))
                
                # Llamar a cada seeder individual
                call_command('seed_estudiantes')
                call_command('seed_cursos')
                call_command('seed_inscripciones')
                # Agrega más llamados a call_command para otros seeders aquí
                
                self.stdout.write(self.style.SUCCESS('Todos los seeders se han ejecutado con éxito.'))
            except Exception as e : 
                 self.stdout.write(self.style.ERROR(f'Ocurrio un error durante la ejecución: {str(e)}'))