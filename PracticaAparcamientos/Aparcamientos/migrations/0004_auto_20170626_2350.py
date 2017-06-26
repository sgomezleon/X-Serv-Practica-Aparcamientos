# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aparcamientos', '0003_auto_20170626_2345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aparcamiento',
            old_name='Accessibilidad',
            new_name='Accesibilidad',
        ),
    ]
