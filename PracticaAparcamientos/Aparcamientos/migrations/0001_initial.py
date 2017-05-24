# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aparcamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Nombre', models.TextField(default='')),
                ('Descripcion', models.TextField(default='')),
                ('Enlace', models.TextField(default='')),
                ('Accessibilidad', models.IntegerField(default='0')),
                ('Nombre_Via', models.TextField(default='')),
                ('Tipo_Via', models.TextField(default='')),
                ('Num', models.IntegerField(default='0')),
                ('Localidad', models.TextField(default='')),
                ('Provincia', models.TextField(default='')),
                ('Codigo_Postal', models.IntegerField(default='0')),
                ('Barrio', models.TextField(default='')),
                ('Distrito', models.TextField(default='')),
                ('Coord_X', models.TextField(default='')),
                ('Coord_Y', models.TextField(default='')),
                ('Latitud', models.TextField(default='')),
                ('Longitud', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Comentario', models.TextField(default='')),
                ('Fecha', models.DateField(auto_now_add=True)),
                ('Aparcamiento', models.ForeignKey(to='Aparcamientos.Aparcamiento')),
                ('Usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
