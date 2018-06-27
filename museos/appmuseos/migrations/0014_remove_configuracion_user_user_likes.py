# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmuseos', '0013_configuracion_user_user_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuracion_user',
            name='user_likes',
        ),
    ]
