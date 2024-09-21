from django.contrib import admin
from django.contrib import admin
from .models import Administrador
from .forms import AdministradorForm
from .models import Usuario, Administrador
# Register your models here.

admin.site.register(Usuario)

class AdministradorAdmin(admin.ModelAdmin):
    form = AdministradorForm
    # Esto es opcional, si quieres mostrar campos específicos en el admin:
    list_display = ['user']

admin.site.register(Administrador, AdministradorAdmin)