from django.db import models

# Create your models here


class ServicioLegal(models.Model):
    class Meta:
        abstract = True

    nombreServicio = models.CharField(max_length=255)
    descripcionServicio = models.TextField()
    _costoServicio = models.IntegerField()

    def MostrarInformacion(self):
        return f'Servicio legal registrado: {self.nombreServicio}'
    
    @property
    def costoServicio(self):
        return self._costoServicio
    
    
    
    
class Divorcio(ServicioLegal):
    duracion = models.CharField(max_length=255)
    
    def MostrarInformacion(self):
        return f"Información sobre el divorcio: {self.descripcionServicio}\nDuración estimada: {self.duracion}\nCosto: {self._costoServicio}"

    
class AsesoriaLegal(ServicioLegal):
    
    especialidad = models.CharField(max_length=255)

    def MostrarInformacion(self):
        return f'Informacion sobre la asesoria: {self.descripcionServicio} \n Asunto: {self.especialidad}'