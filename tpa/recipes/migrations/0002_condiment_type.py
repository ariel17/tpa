# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='condiment',
            name='type',
            field=models.ForeignKey(default=None, verbose_name='Type', to='recipes.CondimentType'),
            preserve_default=False,
        ),
    ]
