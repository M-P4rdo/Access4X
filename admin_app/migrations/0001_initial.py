# Generated by Django 5.0.7 on 2024-09-22 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autenticacion_app', '0005_delete_cargoadmin'),
        ('base_app', '0006_remove_administrador_cargo_administrador_superadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='EdicionUsuario',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base_app.usuario')),
                ('dia', models.DateField(auto_now=True)),
                ('hora', models.TimeField(auto_now=True)),
                ('oldNumDocumento', models.CharField(max_length=100)),
                ('oldNombre', models.CharField(max_length=255)),
                ('oldApellido', models.CharField(max_length=255)),
                ('oldCorreo', models.EmailField(max_length=255)),
                ('oldCargo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autenticacion_app.cargousuario')),
                ('oldEntidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autenticacion_app.entidad')),
                ('oldTipoDocumento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autenticacion_app.tipodocumento')),
            ],
            options={
                'abstract': False,
            },
            bases=('base_app.usuario',),
        ),
    ]
