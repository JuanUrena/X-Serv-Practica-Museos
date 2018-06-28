# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmuseos', '0027_time_like_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museum',
            name='name',
            field=models.CharField(unique=True, max_length=128),
        ),
    ]
