from django.contrib.auth.models import User
from autenticacion_app import models as M_autenticacion
from django.db import models


# Create your models here.
class Persona(models.Model):
    tipoDocumento = models.ForeignKey(M_autenticacion.TipoDocumento, on_delete=models.PROTECT)
    numDocumento = models.CharField(max_length=100)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    entidad = models.ForeignKey(M_autenticacion.Entidad, on_delete=models.PROTECT)
    correo = models.EmailField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return (f"{self.numDocumento} | {self.nombre}")

class Usuario(Persona):
    idUsuario = models.AutoField(primary_key=True)
    cargo = models.ForeignKey(M_autenticacion.CargoUsuario, on_delete=models.PROTECT)

class Administrador(Persona):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='admin_profile')
    idAdmin = models.AutoField(primary_key=True)
    superAdmin = models.BooleanField(default=False)