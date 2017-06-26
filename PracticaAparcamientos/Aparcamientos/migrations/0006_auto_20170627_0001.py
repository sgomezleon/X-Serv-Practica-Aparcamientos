# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aparcamientos', '0005_auto_20170627_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparcamiento',
            name='Numero',
            field=models.TextField(default=''),
        ),
    ]
