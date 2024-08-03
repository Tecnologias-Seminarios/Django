# admi_cursos/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstudianteViewSet, CursoViewSet, InscripcionViewSet, EstudiantesPorCurso

router = DefaultRouter()
router.register(r'estudiantes', EstudianteViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'inscripciones', InscripcionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('curso/<int:curso_id>/estudiantes/', EstudiantesPorCurso.as_view(), name='estudiantes-por-curso'),
]

