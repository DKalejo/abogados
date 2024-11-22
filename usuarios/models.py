from django.db import models

# Create your models here


class ServicioLegal(models.Model):

    nombreServicio = models.CharField(max_length=255)
    descripcionServicio = models.TextField()
    costoServicio = models.IntegerField()

    def MostrarInformacion(self):
        return f'Servicio legal registrado: {self.nombreServicio}'

    def costoConIva(self):
        costoFinal = self.costoServicio * 1.19
        return f'Costo del servicio: {costoFinal}'     
    
class Divorcio(ServicioLegal):
    duracion = models.CharField(max_length=255)

    def MostrarInformacion(self):
        return f'Informacion sobre el divorcio: {self.descripcionServicio} \n Duracion estimada: {self.duracion}'
    
class AsesoriaLegal(ServicioLegal):
    
    especialidad = models.CharField(max_length=255)

    def MostrarInformacion(self):
        return f'Informacion sobre la asesoria: {self.descripcionServicio} \n Asunto: {self.especialidad}'