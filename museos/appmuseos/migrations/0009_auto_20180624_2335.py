# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmuseos', '0008_remove_configuracion_user_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracion_user',
            name='size',
            field=models.IntegerField(default=12),
        ),
    ]
