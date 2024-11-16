from django.urls import path
from .views import *

urlpatterns = [
    path('contratos/registrarCaso/<int:idAbogado>/', RegistroCaso, name = 'RegistrarCaso'),
    path('contratos/casos/<int:pk>',ListaDeCasos, name='CasosDeUsuarios'),
    path('contratos/casos/actualizar/<int:pk>/', ActualizarCaso, name='ActualizarCaso'),
    path('contratos/casos/borrar/<int:pk>/', BorrarCaso, name='BorrarCaso')
]