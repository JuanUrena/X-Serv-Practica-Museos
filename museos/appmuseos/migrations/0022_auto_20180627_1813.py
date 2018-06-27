# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmuseos', '0021_auto_20180626_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coment',
            name='title',
        ),
        migrations.RemoveField(
            model_name='coment',
            name='usuario',
        ),
    ]
