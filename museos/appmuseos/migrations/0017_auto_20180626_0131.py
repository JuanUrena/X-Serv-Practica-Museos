# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmuseos', '0016_auto_20180626_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museum',
            name='accessibility',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='museum',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='museum',
            name='barrio',
            field=models.CharField(null=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='museum',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='museum',
            name='district',
            field=models.CharField(null=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='museum',
            name='horary',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='museum',
            name='mail',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='museum',
            name='number_phone',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='museum',
            name='url',
            field=models.TextField(null=True),
        ),
    ]
