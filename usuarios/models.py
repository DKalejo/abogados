from django.db import models

# Create your models here
class Abogados(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=100)
    estado = models.BooleanField(default=False)
    foto = models.CharField(max_length=255)

    def __str__(self):
        return f'Abogado : {self.nombre + ' ' + self.apellido} \n Especialidad: {self.especialidad}'
    
