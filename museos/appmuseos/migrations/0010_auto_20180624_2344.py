# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appmuseos', '0009_auto_20180624_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion_user',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='configuracion_user',
            name='size',
            field=models.IntegerField(),
        ),
    ]
