from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Usuario
from .serializers import UsuarioSerializer
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @action(detail=False, methods=['post'])
    def cambioContrasena(self, request):
        usuario = request.data.get('usuario')
        contrasena = request.data.get('contrasena')
        nueva_contrasena = request.data.get('nueva_contrasena')
        try:
            usuario = Usuario.objects.get(usuario=usuario)
        except Usuario.DoesNotExist:
            return Response({'status': 'usuario_no_encontrado'}, status=status.HTTP_404_NOT_FOUND)

        if not check_password(contrasena, usuario.contrasena):
            return Response({'status': 'contrasena_incorrecta'}, status=status.HTTP_400_BAD_REQUEST)

        usuario.contrasena = make_password(nueva_contrasena)
        usuario.save()
        return Response({'status': 'contrasena_actualizada'})

