# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appmuseos', '0019_auto_20180626_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page_user',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('page', models.CharField(max_length=64, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='configuracion_user',
            name='page',
        ),
        migrations.AddField(
            model_name='configuracion_user',
            name='color',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='configuracion_user',
            name='size',
            field=models.IntegerField(null=True),
        ),
    ]
