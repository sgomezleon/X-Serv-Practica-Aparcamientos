# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Aparcamientos', '0010_auto_20170627_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSS',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('Titulo', models.TextField(default='Mi pagina')),
                ('Color', models.CharField(max_length=32, default='')),
                ('Tamano', models.IntegerField(default=15)),
                ('Usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
