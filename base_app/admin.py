from django.contrib import admin
from .models import Usuarios, Administradores
# Register your models here.

admin.site.register(Usuarios)
admin.site.register(Administradores)