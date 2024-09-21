from django.db import models

# Create your models here.
class CargoUsuario(models.Model):
    idCargo = models.AutoField(primary_key=True)
    cargo = models.CharField(max_length=255)

    def __str__(self):
        return self.cargo


class Entidad(models.Model):
    idEntidad = models.AutoField(primary_key=True)
    entidad = models.CharField(max_length=330)

    def __str__(self):
        return self.entidad

class TipoDocumento(models.Model):
    idTipoDocumento = models.AutoField(primary_key=True)
    TipoDocumento = models.CharField(max_length=255)

    def __str__(self):
        return self.TipoDocumento