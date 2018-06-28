# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmuseos', '0022_auto_20180627_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time_like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('museum', models.ForeignKey(to='appmuseos.Museum')),
            ],
        ),
    ]
