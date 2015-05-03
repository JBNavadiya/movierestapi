# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie_Metadata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('director', models.CharField(max_length=255)),
                ('imdb_score', models.FloatField()),
                ('_99popularity', models.FloatField()),
                ('genre', models.CharField(max_length=535)),
            ],
        ),
    ]
