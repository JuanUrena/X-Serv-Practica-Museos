# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmuseos', '0025_auto_20180627_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time_like',
            name='user',
        ),
    ]
