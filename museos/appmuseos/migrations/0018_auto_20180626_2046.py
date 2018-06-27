# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('appmuseos', '0017_auto_20180626_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracion_user',
            name='color',
            field=models.CharField(null=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='configuracion_user',
            name='page',
            field=models.CharField(null=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='configuracion_user',
            name='size',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='configuracion_user',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
