# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aparcamientos', '0008_auto_20170627_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='Comentario',
            new_name='Comment',
        ),
    ]
