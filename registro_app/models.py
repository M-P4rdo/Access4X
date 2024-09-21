from base_app import models as M_base
from django.db import models

# Create your models here.
class Registro(models.Model):
    idRegistro = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey(M_base.Usuario, on_delete=models.PROTECT)
    horaIngreso = models.TimeField()
    horaSalida = models.TimeField(blank=True)
    dispositivos = models.JSONField(blank=True)
    dia = models.DateField(auto_now=True)

    def __str__(self):
        return self.idRegistro

class TipoDispositivo(models.Model):
    idTipoDisp = models.AutoField(primary_key=True)
    tipoDisp = models.CharField(max_length=255)

    def __str__(self):
        return self.tipoDisp

class Dispositivo(models.Model):
    idDispositivo = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey(M_base.Usuario, on_delete=models.PROTECT)
    marca = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    idTipoDisp = models.ForeignKey(TipoDispositivo, on_delete=models.PROTECT)
    serial = models.CharField(max_length=330)

    def __str__(self):
        return self.serial


