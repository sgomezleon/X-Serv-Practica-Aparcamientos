# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aparcamientos', '0006_auto_20170627_0001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='Aparcamiento',
            new_name='AparcamientoComentado',
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='Puntuacion',
            field=models.IntegerField(default='0'),
        ),
    ]
