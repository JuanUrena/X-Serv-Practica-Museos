# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmuseos', '0005_auto_20180624_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion_user',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('color', models.CharField(max_length=32)),
                ('page', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='coment',
            name='title',
            field=models.CharField(max_length=64, default='Título'),
        ),
        migrations.AlterField(
            model_name='coment',
            name='text',
            field=models.TextField(default='Comentario'),
        ),
    ]
