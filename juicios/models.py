from django.db import models
from django.contrib.auth.models import User
from usuarios.models import Abogados


class Casos(models.Model):
    TipoCaso = models.CharField(max_length=255)
    Descripcion = models.TextField()
    Fk_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    Fk_abogado = models.ForeignKey(Abogados, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Fk_usuario.username}: {self.TipoCaso} {self.Fk_abogado.nombre}'
    