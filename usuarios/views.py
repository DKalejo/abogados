# Importacion de modelos
from django.contrib.auth.models import User
from .models import Divorcio, AsesoriaLegal

# Importacion de renderizado de vistas
from django.shortcuts import render, redirect

# Importacion de autenticacion del usuario
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Importacion de manejo de errores
from django.db import IntegrityError

# REST API
from rest_framework import viewsets
from .serializers import DivorciosSerializers, AsesoriasLegalesSerializers

UBICACION_LOGUEO = "../Templates/autenticacion/"
UBICACION_USUARIOS = "../Templates/usuarios/"
UBICACION_SERVICIOS = "../Templates/servicios/"
UBICACION_DIVORCIOS = "../Templates/servicios/divorcios/"
UBICACION_ASESORIAS = "../Templates/servicios/asesorias/"


# Create your views here

class DivorciosViewSet(viewsets.ModelViewSet):
    queryset = Divorcio.objects.all()
    serializer_class = DivorciosSerializers

class AsesoriasLegalesViewSet(viewsets.ModelViewSet):
    queryset = AsesoriaLegal.objects.all()
    serializer_class = AsesoriasLegalesSerializers

# Logica para las vistas para el registrar y iniciar
class VistasUsuario:

    def __init__(self,request):
        self.request = request

    def Registro(self):
        if self.request.POST["pass1"] == self.request.POST["pass2"]:
            nombre = self.request.POST["nombre"]
            contra = self.request.POST["pass1"]
            ModelUser = User.objects.create_user(username=nombre, password=contra)
            try:
                ModelUser.save()
                login(self.request, ModelUser)
                return redirect("Dashboard")
            except IntegrityError:
                return render(
                    self.request,
                    f"{UBICACION_LOGUEO}registrarse.html",
                    {"Error": "Usuario creado"},
                )
        else:
            return render(
                self.request,
                f"{UBICACION_LOGUEO}registrarse.html",
                {"Error": "Las contraseñas no coinciden"},
            )

    def InicioSesion(self):
        nombre = self.request.POST["nombre"]
        contra = self.request.POST["pass"]
        auth = authenticate(username=nombre, password=contra)
        if auth is not None:
            login(self.request, auth)
            return redirect("Dashboard")
        else:
            return render(
                self.request,
                f"{UBICACION_LOGUEO}iniciar_sesion.html",
                {"Error": "Usuario o contraseña no coinciden"},
            )

    def CierreSesion(self):
        logout(self.request)
        return redirect("Inicio")

# Logica para las vistas de los servicios
class VistaDeServiciosLegales:

    @staticmethod
    def RegistroServicio(request,model):

        # Obtencion de datos desde el formulario
        servicioFormulario = request.POST["Servicio"]
        DescripcionFormulario = request.POST["Descripcion"]
        CostoServicio = request.POST["Costo"]

        # Guardado de datos
        try:
            model.objects.create(
                nombreServicio=servicioFormulario,
                descripcionServicio=DescripcionFormulario,
                costoServicio=CostoServicio,
            )
            return f"Servicio registrado exitosamente"
        except IntegrityError:
            return "Error: no se pudo guardar el caso"

    @staticmethod
    def ListaDeServicios(model):
            return model.objects.all()

    @staticmethod
    def DetallesDeServicios(model,pk):
        return model.objects.get(id=pk)

    @staticmethod
    def ActualizarServicios(request,model,pk):
        ServicioActualizar = model.objects.get(id=pk)
        try:
            ServicioActualizar.nombreServicio = request.POST["Servicio"]
            ServicioActualizar.descripcionServicio = request.POST["Descripcion"]
            ServicioActualizar.costoServicio = request.POST["Costo"]
            ServicioActualizar.save()
        except IntegrityError:
            return f"Error al actualizar"

    @staticmethod
    def BorrarServicio(model, pk):
        try:
            servicio = model.objects.get(id=pk)
            servicio.delete()
        except IntegrityError:
            return "Error al borrar"

# Logica para las vistas de divocios

class VistaDeDivorcios(VistaDeServiciosLegales):

    @staticmethod
    def RegistroDivorcios(request, model):
        servicio = request.POST['Servicio']
        descripcion = request.POST['Descripcion']
        costo = request.POST['Costo']
        duracion = request.POST['Duracion']

        try:
            model.objects.create(
                nombreServicio = servicio,
                descripcionServicio = descripcion,
                costoServicio = costo,
                duracion = duracion
            )
        except:
            return 'Error'
        
    @staticmethod
    def ListaDivorcios(model):
        return VistaDeServiciosLegales.ListaDeServicios(model)
    
    @staticmethod
    def DetallesDivorcios(model,pk):
        return VistaDeServiciosLegales.DetallesDeServicios(model,pk)
    
    @staticmethod
    def ActualizarDivorcio(request,model,pk):
        DivorcioActualizar = model.objects.get(id=pk)
        try:
            DivorcioActualizar.nombreServicio = request.POST["Servicio"]
            DivorcioActualizar.descripcionServicio = request.POST["Descripcion"]
            DivorcioActualizar.costoServicio = request.POST["Costo"]
            DivorcioActualizar.duracion = request.POST['Duracion']
            DivorcioActualizar.save()
        except IntegrityError:
            return f"Error al actualizar"

    @staticmethod
    def BorrarDivorcio(model,pk):
        try:
            divorcio = model.objects.get(id=pk)
            divorcio.delete()
        except IntegrityError:
            return "Error al borrar"

class VistaDeAsesoriasLegales(VistaDeServiciosLegales):

    @staticmethod
    def RegistroAsesorias(request, model):
        servicio = request.POST['Servicio']
        descripcion = request.POST['Descripcion']
        costo = request.POST['Costo']
        especialidad = request.POST['Especialidad']

        try:
            model.objects.create(
                nombreServicio = servicio,
                descripcionServicio = descripcion,
                costoServicio = costo,
                especialidad = especialidad
            )
        except:
            return 'Error'
        
    @staticmethod
    def ListaAsesorias(model):
        return VistaDeServiciosLegales.ListaDeServicios(model)
    
    @staticmethod
    def DetallesAsesorias(model,pk):
        return VistaDeServiciosLegales.DetallesDeServicios(model,pk)
    
    @staticmethod
    def ActualizarAsesorias(request,model,pk):
        AsesoriaActualizar = model.objects.get(id=pk)
        try:
            AsesoriaActualizar.nombreServicio = request.POST["Servicio"]
            AsesoriaActualizar.descripcionServicio = request.POST["Descripcion"]
            AsesoriaActualizar.costoServicio = request.POST["Costo"]
            AsesoriaActualizar.especialidad = request.POST['Especialidad']
            AsesoriaActualizar.save()
        except IntegrityError:
            return f"Error al actualizar"

    @staticmethod
    def BorrarAsesorias(model,pk):
        try:
            divorcio = model.objects.get(id=pk)
            divorcio.delete()
        except IntegrityError:
            return "Error al borrar"

# Vistas

def RegistrosUsuarios(request):
    if request.method == "GET":
        return render(request, f"{UBICACION_LOGUEO}registrarse.html")
    else:
        Usuarios = VistasUsuario(request)
        return Usuarios.Registro()

def InicioSesionUsuarios(request):
    if request.method == "GET":
        return render(request, f"{UBICACION_LOGUEO}iniciar_sesion.html")
    else:
        Usuarios = VistasUsuario(request)
        return Usuarios.InicioSesion()

def CerrarSesion(request):
    Usuarios = VistasUsuario(request)
    return Usuarios.CierreSesion()

@login_required
def Dashboard(request):
    Divorcios = VistaDeDivorcios.ListaDivorcios(Divorcio)
    Asesorias = VistaDeAsesoriasLegales.ListaAsesorias(AsesoriaLegal)
    if (Divorcios != None ) or (Asesorias != None):
        return render(request, f"{UBICACION_USUARIOS}dashboard.html", {'Divorcios':Divorcios, 'Asesorias':Asesorias})

# VISTAS DE SERVICIOS
@login_required
def RegistroDivorcios(request):
    if request.method == 'GET':
        return render(request,f'{UBICACION_DIVORCIOS}registrar_divorcio.html')
    else:
        VistaDeDivorcios.RegistroDivorcios(request,Divorcio)
        return redirect('Dashboard')

@login_required
def ActualizarDivorcios(request, pk):
    if request.method == "GET":
        print(request)
        datosFormulario = VistaDeDivorcios.DetallesDivorcios(Divorcio,pk)
        return render(
            request,
            f"{UBICACION_DIVORCIOS}actualizar_divorcio.html",
            {"DatosFormulario": datosFormulario},
        )
    else:
        VistaDeDivorcios.ActualizarDivorcio(request,Divorcio,pk)
        return redirect("Dashboard")

@login_required
def BorrarDivorcios(request, pk):
    if request.method == "GET":
        return render(request, f"{UBICACION_DIVORCIOS}confirmacion_borrar.html")
    else:
        VistaDeDivorcios.BorrarDivorcio(Divorcio,pk)
        return redirect("Dashboard")
    
@login_required
def RegistroAsesorias(request):
    if request.method == 'GET':
        return render(request,f'{UBICACION_ASESORIAS}registrar_asesoria.html')
    else:
        VistaDeAsesoriasLegales.RegistroAsesorias(request,AsesoriaLegal)
        return redirect('Dashboard')

@login_required
def ActualizarAsesorias(request, pk):
    if request.method == "GET":
        print(request)
        datosFormulario = VistaDeAsesoriasLegales.DetallesAsesorias(AsesoriaLegal,pk)
        return render(
            request,
            f"{UBICACION_ASESORIAS}actualizar_asesoria.html",
            {"DatosFormulario": datosFormulario},
        )
    else:
        VistaDeAsesoriasLegales.ActualizarAsesorias(request,AsesoriaLegal,pk)
        return redirect("Dashboard")

@login_required
def BorrarAsesorias(request, pk):
    if request.method == "GET":
        return render(request, f"{UBICACION_ASESORIAS}confirmacion_borrar.html")
    else:
        VistaDeAsesoriasLegales.BorrarAsesorias(AsesoriaLegal,pk)
        return redirect("Dashboard")

