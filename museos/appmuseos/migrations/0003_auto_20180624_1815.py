# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appmuseos', '0002_auto_20180624_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='museum',
            name='num_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='museum',
            name='user_likes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
