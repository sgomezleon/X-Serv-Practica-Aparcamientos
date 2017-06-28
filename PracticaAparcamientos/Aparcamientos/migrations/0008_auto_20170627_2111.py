# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Aparcamientos', '0007_auto_20170627_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seleccionado',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('Fecha', models.DateField(auto_now_add=True)),
                ('Favorito', models.IntegerField(default='0')),
            ],
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='Cantidad',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='seleccionado',
            name='Elegido',
            field=models.ForeignKey(to='Aparcamientos.Aparcamiento'),
        ),
        migrations.AddField(
            model_name='seleccionado',
            name='Usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
