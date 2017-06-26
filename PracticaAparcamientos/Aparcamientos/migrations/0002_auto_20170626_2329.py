# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aparcamientos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aparcamiento',
            name='Coord_X',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='Coord_Y',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='Provincia',
        ),
    ]
