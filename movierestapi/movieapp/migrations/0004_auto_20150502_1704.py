# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import movierestapi.movieapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_auto_20150502_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_metadata',
            name='_99popularity',
            field=movierestapi.movieapp.models.customFloatField(null=True, blank=True),
        ),
    ]
