from django.contrib import admin
from .models import Registros, TipoDispositivo, Dispositivos
# Register your models here.

admin.site.register(Registros)
admin.site.register(TipoDispositivo)
admin.site.register(Dispositivos)