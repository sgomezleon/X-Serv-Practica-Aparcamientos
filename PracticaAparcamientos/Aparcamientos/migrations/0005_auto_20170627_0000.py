# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aparcamientos', '0004_auto_20170626_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparcamiento',
            name='Numero',
            field=models.IntegerField(default=''),
        ),
    ]
