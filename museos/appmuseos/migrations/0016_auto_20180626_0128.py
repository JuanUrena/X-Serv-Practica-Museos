# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmuseos', '0015_configuracion_user_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museum',
            name='transport',
            field=models.TextField(default='No Data', null=True),
        ),
    ]
