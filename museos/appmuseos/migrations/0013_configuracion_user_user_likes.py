# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appmuseos', '0012_auto_20180624_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion_user',
            name='user_likes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
