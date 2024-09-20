from autenticacion_app import models as M_autenticacion
from django.db import models


# Create your models here.
class Persona(models.Model):
    tipoDocumento = models.CharField(max_length=255)
    numDocumento = models.CharField(max_length=100)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    entidad = models.OneToOneField(M_autenticacion.Entidades, on_delete=models.PROTECT)
    cargo = models.OneToOneField(M_autenticacion.Cargos, on_delete=models.PROTECT)
    correo = models.CharField(max_length=255)

    class Meta:
        abstract = True

class Usuarios(Persona):
    idUsuario = models.AutoField(primary_key=True)

class Administradores(Persona):
    idAdmin = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=255)