from django.contrib import admin

from mi_aplicacion.models import Escuela, Maestro, Alumno

admin.site.register(Escuela)
admin.site.register(Maestro)
admin.site.register(Alumno)