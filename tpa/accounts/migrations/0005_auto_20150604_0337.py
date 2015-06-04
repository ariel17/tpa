# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20150604_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='complexion',
            field=models.CharField(max_length=1, null=True, verbose_name='Complexion', choices=[(b'l', 'Little'), (b'm', 'Middle'), (b'b', 'Big')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='conditions',
            field=models.ManyToManyField(help_text='Existent health conditions', to='health.Condition', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='diets',
            field=models.ManyToManyField(help_text='What kind of diets do you prefer?', to='health.DietType', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='preferences',
            field=models.ManyToManyField(help_text='What kind of food do you like?', to='recipes.Ingredient', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rutine',
            field=models.CharField(max_length=1, null=True, verbose_name='Rutine', choices=[(b's', 'Sedentary with some exercise (-30 min)'), (b'n', 'Sedentary without exercise'), (b'm', 'Sedentary with exercise (+30 min)'), (b'i', 'Active with extra exercise (+30 min)')]),
        ),
    ]
