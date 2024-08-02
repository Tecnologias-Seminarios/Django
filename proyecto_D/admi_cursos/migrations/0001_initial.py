# Generated by Django 5.0.7 on 2024-08-02 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('usuario', models.CharField(max_length=50, unique=True)),
                ('contrasena', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Inscripciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inscripcion', models.DateField()),
                ('estado', models.CharField(choices=[('activo', 'Activo'), ('completado', 'Completado'), ('cancelado', 'Cancelado'), ('en espera', 'En espera')], default='activo', max_length=10)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admi_cursos.cursos')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admi_cursos.estudiantes')),
            ],
        ),
    ]
