# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import movierestapi.movieapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_metadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_metadata',
            name='imdb_score',
            field=movierestapi.movieapp.models.customFloatField(null=True, blank=True),
        ),
    ]
