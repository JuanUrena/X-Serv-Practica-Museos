# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmuseos', '0004_auto_20180624_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='museum',
            name='accessibility',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='museum',
            name='address',
            field=models.TextField(default='No Data'),
        ),
        migrations.AddField(
            model_name='museum',
            name='barrio',
            field=models.CharField(max_length=32, default='No Data'),
        ),
        migrations.AddField(
            model_name='museum',
            name='description',
            field=models.TextField(default='No Data'),
        ),
        migrations.AddField(
            model_name='museum',
            name='district',
            field=models.CharField(max_length=32, default='No Data'),
        ),
        migrations.AddField(
            model_name='museum',
            name='horary',
            field=models.TextField(default='No Data'),
        ),
        migrations.AddField(
            model_name='museum',
            name='mail',
            field=models.TextField(default='No Data'),
        ),
        migrations.AddField(
            model_name='museum',
            name='number_phone',
            field=models.TextField(default='No Data'),
        ),
        migrations.AddField(
            model_name='museum',
            name='transport',
            field=models.TextField(default='No Data'),
        ),
        migrations.AddField(
            model_name='museum',
            name='url',
            field=models.TextField(default='No Data'),
        ),
    ]
