# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmuseos', '0020_auto_20180626_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracion_user',
            name='color',
            field=models.CharField(max_length=32, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion_user',
            name='size',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='page_user',
            name='page',
            field=models.CharField(max_length=64, blank=True, null=True),
        ),
    ]
