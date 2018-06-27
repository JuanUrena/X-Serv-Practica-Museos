# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmuseos', '0011_remove_configuracion_user_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracion_user',
            name='color',
            field=models.CharField(default='color', max_length=32),
        ),
        migrations.AlterField(
            model_name='configuracion_user',
            name='page',
            field=models.CharField(default='Mi pagina', max_length=64),
        ),
    ]
