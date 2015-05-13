# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
        ('health', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistic',
            name='recipe',
            field=models.ForeignKey(verbose_name='Recipe', to='recipes.Recipe'),
        ),
        migrations.AddField(
            model_name='statistic',
            name='user',
            field=models.OneToOneField(verbose_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='conditions',
            field=models.ManyToManyField(help_text='Existent health conditions', to='health.Condition'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(verbose_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='history',
            name='recipe',
            field=models.ForeignKey(verbose_name='Recipe', to='recipes.Recipe'),
        ),
        migrations.AddField(
            model_name='history',
            name='user',
            field=models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='classification',
            name='recipe',
            field=models.ForeignKey(verbose_name='Recipe', to='recipes.Recipe'),
        ),
        migrations.AddField(
            model_name='classification',
            name='user',
            field=models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL),
        ),
    ]
