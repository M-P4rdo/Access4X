from django.contrib import admin
from .models import Cargo, Entidad, TipoDocumento
# Register your models here.

admin.site.register(Cargo)
admin.site.register(Entidad)
admin.site.register(TipoDocumento)