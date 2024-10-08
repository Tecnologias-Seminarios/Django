from django.contrib import admin
from .models import Usuario

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nombre', 'apellidos', 'edad', 'fecha_nacimiento')
    search_fields = ('usuario', 'nombre', 'apellidos')



