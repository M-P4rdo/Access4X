# Generated by Django 5.0.7 on 2024-09-21 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion_app', '0004_rename_entidades_entidad'),
        ('base_app', '0006_remove_administrador_cargo_administrador_superadmin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CargoAdmin',
        ),
    ]