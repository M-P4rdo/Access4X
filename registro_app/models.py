from base_app import models as M_base
from django.db import models

# Create your models here.
class Registros(models.Model):
    idRegistro = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey(M_base.Usuarios, on_delete=models.PROTECT)
    horaIngreso = models.TimeField()
    horaSalida = models.TimeField(blank=True)
    dispositivos = models.JSONField(blank=True)
    dia = models.DateField(auto_now=True)

class TipoDispositivo(models.Model):
    idTipoDisp = models.AutoField(primary_key=True)
    tipoDisp = models.CharField(max_length=255)

class Dispositivos(models.Model):
    idDispositivo = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey(M_base.Usuarios, on_delete=models.PROTECT)
    marca = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    idTipoDisp = models.OneToOneField(TipoDispositivo, on_delete=models.PROTECT)
    serial = models.CharField(max_length=330)


