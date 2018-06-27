# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmuseos', '0010_auto_20180624_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuracion_user',
            name='user',
        ),
    ]
