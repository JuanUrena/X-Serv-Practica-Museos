# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmuseos', '0014_remove_configuracion_user_user_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion_user',
            name='user',
            field=models.CharField(unique=True, default='user', max_length=32),
            preserve_default=False,
        ),
    ]
