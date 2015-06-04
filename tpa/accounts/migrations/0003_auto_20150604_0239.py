# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_condiment_type'),
        ('health', '0001_initial'),
        ('accounts', '0002_auto_20150513_0423'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='diets',
            field=models.ManyToManyField(help_text='What kind of diets do you prefer?', to='health.DietType'),
        ),
        migrations.AddField(
            model_name='profile',
            name='preferences',
            field=models.ManyToManyField(help_text='What kind of food do you like?', to='recipes.Ingredient'),
        ),
        migrations.AddField(
            model_name='profile',
            name='rutine',
            field=models.CharField(default=None, max_length=1, verbose_name='Rutine', choices=[(b's', 'Sedentary with some exercise (-30 min)'), (b'n', 'Sedentary without exercise'), (b'm', 'Sedentary with exercise (+30 min)'), (b'i', 'Active with extra exercise (+30 min)')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.FloatField(help_text='In meters', verbose_name='Height'),
        ),
    ]
