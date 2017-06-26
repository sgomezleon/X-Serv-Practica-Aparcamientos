# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aparcamientos', '0002_auto_20170626_2329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aparcamiento',
            old_name='Tipo_Via',
            new_name='Clase_Via',
        ),
        migrations.RenameField(
            model_name='aparcamiento',
            old_name='Num',
            new_name='Numero',
        ),
    ]
