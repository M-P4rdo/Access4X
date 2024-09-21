# Generated by Django 5.0.7 on 2024-09-21 01:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion_app', '0002_cargousuario_rename_cargos_cargoadmin'),
        ('base_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administradores',
            name='cargo',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='cargo',
        ),
        migrations.AlterField(
            model_name='administradores',
            name='entidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autenticacion_app.entidades'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='entidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autenticacion_app.entidades'),
        ),
    ]