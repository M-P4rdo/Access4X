# Generated by Django 5.0.7 on 2024-09-22 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_edicionusuario_admin_edicionusuario_idedicion_and_more'),
        ('autenticacion_app', '0005_delete_cargoadmin'),
        ('base_app', '0006_remove_administrador_cargo_administrador_superadmin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CargoUsuario',
            new_name='Cargo',
        ),
    ]
