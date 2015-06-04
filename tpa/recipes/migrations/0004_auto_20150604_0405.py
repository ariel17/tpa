# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20150604_0333'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='title',
            field=models.CharField(default=None, max_length=100, verbose_name='Title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(verbose_name='User', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
