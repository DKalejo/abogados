from django.urls import path
from .views import *
from juicios.views import * 

urlpatterns = [
    # URL de usuarios normales
    path('accounts/Registrarse/', RegistrosUsuarios, name='RegistroUsuarios'),
    path('accounts/Iniciar Sesion/', InicioSesionUsuarios, name='IniciarSesionUsuarios'),
    path('accounts/Cerrar Sesion/',CerrarSesion, name='CerrarSesion'),
    path('dashboard/User/',DashboardUser, name='DashboardUser'),
    path('dashboard/Admin/',DashboardAdmin, name='DashboardAdmin'),


    # URL de superAdmin
    path('crearAbogados/',CrearAbogados,name='CrearAbogados'),
    path('detallesAbogados/<int:pk>', DetallesAbogados, name='DetallesAbogados'),
    path('actualizarAbogado/<int:pk>',ActualizarAbogados, name='ActualizarAbogados'),
    path('borrarAbogado/<int:pk>',BorrarAbogados, name='BorrarAbogados'),    
]
