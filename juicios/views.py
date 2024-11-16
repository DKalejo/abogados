from django.shortcuts import render, get_object_or_404, redirect
from .models import Casos
from usuarios.models import Abogados
from usuarios.views import (
    UBICACION_CASOS,
)
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.


class VistaDeCasos:
    def __init__(self, request):
        self.request = request

    def RegistroCaso(self, idAbogado):

        # Obtencion de datos desde el formulario
        abogado = get_object_or_404(Abogados, id=idAbogado)
        TipoCasoFormulario = self.request.POST["TipoCaso"]
        DescripcionFormulario = self.request.POST["Descripcion"]
        usuario = self.request.user

        # Guardado de datos
        try:
            caso = Casos.objects.create(
                TipoCaso=TipoCasoFormulario,
                Descripcion=DescripcionFormulario,
                Fk_usuario=usuario,
                Fk_abogado=abogado,
            )
            if caso:
                abogado.estado = True
                abogado.save()
            return f"Caso registrado exitosamente al abogado {abogado.nombre + abogado.apellido}"
        except IntegrityError:
            return "Error: no se pudo guardar el caso"

    def ListaDeCasos(self, pk):
        casos = Casos.objects.filter(Fk_usuario=pk)
        return casos

    def DetallesDeCasos(self, pk):
        detallesCaso = Casos.objects.get(id=pk)
        return detallesCaso

    def ActualizarCaso(self, pk):
        casoActualizar = Casos.objects.get(id=pk)
        try:
            casoActualizar.TipoCaso = self.request.POST["TipoCaso"]
            casoActualizar.Descripcion = self.request.POST["Descripcion"]
            casoActualizar.save()
        except IntegrityError:
            return f'Error al actualizar'
    
    def BorrarCaso(self, pk_caso):
        try:
            caso = Casos.objects.get(id = pk_caso)
            abogado = Abogados.objects.get(id = caso.Fk_abogado.id)
            abogado.estado = False
            abogado.save()
            caso.delete()
        except IntegrityError:
            return 'Error al borrar'

@login_required
def RegistroCaso(request, idAbogado):
    vistaCasos = VistaDeCasos(request)
    if request.method == "GET":
        return render(request, f"{UBICACION_CASOS}registrar_caso.html")
    else:
        vistaCasos.RegistroCaso(idAbogado)
        return redirect("DashboardUser")

@login_required
def ListaDeCasos(request, pk):
    vistaCasos = VistaDeCasos(request)
    CasosDelUsuario = vistaCasos.ListaDeCasos(pk)
    return render(
        request,
        f"{UBICACION_CASOS}casos_usuarios.html",
        {"CasosDelUsuario": CasosDelUsuario},
    )

@login_required
def ActualizarCaso(request, pk):
    vistaCasos = VistaDeCasos(request)
    if request.method == "GET":
        datosFormulario = vistaCasos.DetallesDeCasos(pk)
        return render(
            request,
            f"{UBICACION_CASOS}actualizar_caso.html",
            {"DatosFormulario": datosFormulario},
        )
    else:
        vistaCasos.ActualizarCaso(pk)
        return redirect("CasosDeUsuarios", pk = request.user.id )

@login_required
def BorrarCaso(request, pk):
    vistaCaso= VistaDeCasos(request)
    if request.method == 'GET':
        return render(request,f'{UBICACION_CASOS}confirmacion_borrar.html')
    else:
        vistaCaso.BorrarCaso(pk)
        return redirect("CasosDeUsuarios", pk = request.user.id )