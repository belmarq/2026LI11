from django.urls import include, path
from rest_framework import routers
from mi_aplicacion.views import Home, Escuelas, EscuelaAlta, EscuelaEditar, EscuelaEliminar, MaestroAlta, MaestroEliminar, Maestros, MaestroEditar
from mi_aplicacion.viewsets import AlumnoViewSet, EscuelaViewSet, MaestroViewSet

router = routers.DefaultRouter()
router.register(r'escuelas', EscuelaViewSet)
router.register(r'maestros', MaestroViewSet)
router.register(r'alumnos', AlumnoViewSet)


urlpatterns = [
    path("", Home.as_view(), name='home'),
    path("api/", include(router.urls)),
    path("escuelas", Escuelas.as_view(), name='escuelas'),
    path("escuelas_alta", EscuelaAlta.as_view(), name='escuelas_alta'),    
    path("escuelas_editar/<int:id>", EscuelaEditar.as_view(), name='escuelas_editar'),        
    path("escuelas_eliminar/<int:id>", EscuelaEliminar.as_view(), name='escuelas_eliminar'),
    path("maestros", Maestros.as_view(), name='maestros'),
    path("maestros_alta", MaestroAlta.as_view(), name='maestros_alta'),
    path("maestros_editar/<int:id>", MaestroEditar.as_view(), name='maestros_editar'),
    path("maestros_eliminar/<int:id>", MaestroEliminar.as_view(), name='maestros_eliminar'),

]