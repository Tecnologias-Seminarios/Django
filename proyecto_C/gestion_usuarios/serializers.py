# gestion_usuarios/serializers.py
from rest_framework import serializers
from .models import Usuario
from django.contrib.auth.hashers import make_password


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'usuario', 'nombre', 'apellidos', 'edad', 'fecha_nacimiento', 'contrasena']
        extra_kwargs = {
            'contrasena': {'write_only': True}
        }


    def create(self, validated_data):
        validated_data['contrasena'] = make_password(validated_data['contrasena'])
        return super(UsuarioSerializer, self).create(validated_data)


    def update(self, instance, validated_data):
        if 'contrasena' in validated_data:
            validated_data['contrasena'] = make_password(validated_data['contrasena'])
        return super(UsuarioSerializer, self).update(instance, validated_data)