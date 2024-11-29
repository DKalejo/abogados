from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'divorcios',DivorciosViewSet, basename='divorcios')
router.register(r'asesoriasLegales',AsesoriasLegalesViewSet,basename='asesoriasLegales')





urlpatterns = [
    # URL de usuarios normales
    path('accounts/Registrarse/', RegistrosUsuarios, name='RegistroUsuarios'),
    path('accounts/Iniciar Sesion/', InicioSesionUsuarios, name='IniciarSesionUsuarios'),
    path('accounts/Cerrar Sesion/',CerrarSesion, name='CerrarSesion'),
    path('dashboard/',Dashboard, name='Dashboard'),

    # URL de divorcios
    path('contratos/divorcios/registrar/', RegistroDivorcios, name = 'RegistrarDivorcios'),
    path('contratos/divorcios/actualizar/<int:pk>/', ActualizarDivorcios, name='ActualizarDivorcios'),
    path('contratos/divorcios/borrar/<int:pk>/', BorrarDivorcios, name='BorrarDivorcios'),

    # URL de Asesorias
    path('contratos/asesorias/registrar/', RegistroAsesorias, name = 'RegistrarAsesorias'),
    path('contratos/asesorias/actualizar/<int:pk>/', ActualizarAsesorias, name='ActualizarAsesorias'),
    path('contratos/asesorias/borrar/<int:pk>/', BorrarAsesorias, name='BorrarAsesorias'), 

    # API
    path('api/v1/', include(router.urls))         
]
