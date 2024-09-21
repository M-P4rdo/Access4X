from django.contrib import admin
from .models import Registro, TipoDispositivo, Dispositivo
# Register your models here.

admin.site.register(Registro)
admin.site.register(TipoDispositivo)
admin.site.register(Dispositivo)