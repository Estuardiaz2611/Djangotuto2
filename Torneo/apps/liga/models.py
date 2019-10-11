from django.db import models

# Create your models here.

class Liga(models.Model):
    nombre_liga = models.CharField(max_length=50)
    genero = models.CharField(max_length=10)
    categoria = models.CharField(max_length=10)
    jugadores = models.IntegerField()
    fecha_inicio = models.DateField()

    def __str__(self):
        return '{}'.format(self.nombre_liga)