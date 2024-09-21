from django.contrib import admin
from .models import CargoUsuario, Entidad, TipoDocumento
# Register your models here.

admin.site.register(CargoUsuario)
admin.site.register(Entidad)
admin.site.register(TipoDocumento)