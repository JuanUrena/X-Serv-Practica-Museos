# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmuseos', '0018_auto_20180626_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuracion_user',
            name='color',
        ),
        migrations.RemoveField(
            model_name='configuracion_user',
            name='size',
        ),
    ]
