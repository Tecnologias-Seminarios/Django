# admi_cursos/views.py
from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Estudiantes, Cursos, Inscripciones
from .serializers import EstudianteSerializer, CursoSerializer, InscripcionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiantes.objects.all()
    serializer_class = EstudianteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursoSerializer

class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripciones.objects.all()
    serializer_class = InscripcionSerializer

class EstudiantesPorCurso(APIView):
    def get(self, request, curso_id):
        # Asegura que el curso existe, si no, retorna 404
        curso = get_object_or_404(Cursos, pk=curso_id)
        # Utiliza prefetch_related para optimizar la carga de datos relacionados
        inscripciones = Inscripciones.objects.filter(curso=curso).prefetch_related('estudiante')
        estudiantes = [inscripcion.estudiante for inscripcion in inscripciones]
        serializer = EstudianteSerializer(estudiantes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)