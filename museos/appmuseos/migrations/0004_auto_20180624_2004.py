# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmuseos', '0003_auto_20180624_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museum',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
