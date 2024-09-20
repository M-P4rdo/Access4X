from django.db import models

# Create your models here.
class Cargos(models.Model):
    idCargo = models.AutoField(primary_key=True)
    cargo = models.CharField(max_length=255)

class Entidades(models.Model):
    idEntidad = models.AutoField(primary_key=True)
    entidad = models.CharField(max_length=330)