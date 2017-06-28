# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Aparcamientos', '0009_auto_20170627_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentarioAparcamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.TextField(default='')),
                ('Fecha', models.DateField(auto_now_add=True)),
                ('AparcamientoComentado', models.ForeignKey(to='Aparcamientos.Aparcamiento')),
                ('Usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='AparcamientoComentado',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='Usuario',
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]
