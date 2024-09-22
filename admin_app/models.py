from base_app import models as M_base
from django.db import models

# Create your models here.
class EdicionUsuario(M_base.Persona):
    idEdicion = models.AutoField(primary_key=True)
    dia = models.DateField(auto_now=True)
    hora = models.TimeField(auto_now=True)
    admin = models.ForeignKey(M_base.Administrador, on_delete=models.PROTECT)
    tipoDocumento = models.CharField(max_length=50)
    oldTipoDocumento = models.CharField(max_length=50)
    oldNumDocumento = models.CharField(max_length=100)
    oldNombre = models.CharField(max_length=255)
    oldApellido = models.CharField(max_length=255)
    oldEntidad = models.CharField(max_length=100)
    oldCorreo = models.CharField(max_length=320)
    cargo = models.CharField(max_length=255)
    oldCargo = models.CharField(max_length=255)
    entidad = models.CharField(max_length=100)

class EliminacionUsuario(M_base.Persona):
    idEliminacion = models.AutoField(primary_key=True)
    dia = models.DateField(auto_now=True)
    hora = models.TimeField(auto_now=True)
    admin = models.ForeignKey(M_base.Administrador, on_delete=models.PROTECT)
    tipoDocumento = models.CharField(max_length=50)
    entidad = models.CharField(max_length=100)
