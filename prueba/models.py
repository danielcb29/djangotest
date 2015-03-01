from django.db import models

# Create your models here.

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=60)

    def __unicode__(self):
        return self.nombre

class Investigador(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    laboratorio = models.ManyToManyField(Laboratorio)
