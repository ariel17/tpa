# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20150604_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rutine',
            field=models.CharField(default=None, max_length=1, verbose_name='Rutine', choices=[(b's', 'Sedentary with some exercise (-30 min)'), (b'n', 'Sedentary without exercise'), (b'm', 'Sedentary with exercise (+30 min)'), (b'i', 'Active with extra exercise (+30 min)')]),
            preserve_default=False,
        ),
    ]
