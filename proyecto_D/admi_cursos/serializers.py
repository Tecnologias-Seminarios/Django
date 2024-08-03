#admi_cursos/serializers.py
from .models import Estudiantes, Cursos, Inscripciones
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiantes
        fields = ['id', 'usuario', 'nombre', 'apellidos', 'edad', 'fecha_nacimiento', 'contrasena']
        extra_kwargs = {
            'contrasena': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['contrasena'] = make_password(validated_data['contrasena'])
        return super(EstudianteSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        if 'contrasena' in validated_data:
            validated_data['contrasena'] = make_password(validated_data['contrasena'])
        return super(EstudianteSerializer, self).update(instance, validated_data)

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = ['id', 'nombre', 'descripcion']

class InscripcionSerializer(serializers.ModelSerializer):
    estudiante = EstudianteSerializer(read_only=True)
    estudiante_id = serializers.PrimaryKeyRelatedField(
        queryset=Estudiantes.objects.all(), source='estudiante', write_only=True)
    curso = CursoSerializer(read_only=True)
    curso_id = serializers.PrimaryKeyRelatedField(
        queryset=Cursos.objects.all(), source='curso', write_only=True)

    class Meta:
        model = Inscripciones
        fields = ['id', 'estudiante', 'estudiante_id', 'curso', 'curso_id', 'fecha_inscripcion', 'estado']
