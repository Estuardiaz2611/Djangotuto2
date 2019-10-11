from django.db import models

from apps.liga.models import Liga

class Equipo(models.Model):

    nombre_equipo = models.CharField(max_length=50)
    siglas = models.CharField(max_length=5)
    jugadores = models.IntegerField()
    encargado = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    
    liga = models.ForeignKey(Liga, null=True, blank=True, on_delete=models.CASCADE)