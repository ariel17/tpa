# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20150604_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='weight',
            field=models.FloatField(default=None, help_text='In Kg.', verbose_name='Weight'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.FloatField(help_text='In meters.', verbose_name='Height'),
        ),
    ]
