# Generated by Django 5.0.7 on 2024-09-21 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion_app', '0004_rename_entidades_entidad'),
        ('base_app', '0003_administradores_cargo_usuarios_cargo_and_more'),
        ('registro_app', '0002_alter_dispositivos_idtipodisp_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Administradores',
            new_name='Administrador',
        ),
        migrations.RenameModel(
            old_name='Usuarios',
            new_name='Usuario',
        ),
    ]
