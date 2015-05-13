# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='DietType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='IdealWeight',
            fields=[
                ('sex', models.CharField(max_length=1, serialize=False, verbose_name='Sex', primary_key=True, choices=[(b'm', 'Male'), (b'f', 'Female')])),
                ('height', models.PositiveSmallIntegerField(help_text='In cm.', verbose_name='Height')),
                ('chest_measure', models.PositiveSmallIntegerField(help_text='In cm.', verbose_name='Chest measure')),
                ('slim_measure', models.PositiveSmallIntegerField(help_text='In cm.', verbose_name='Slim measure')),
                ('hip_measure', models.PositiveSmallIntegerField(help_text='In cm.', verbose_name='Hip measure')),
                ('max_weight', models.SmallIntegerField(help_text='In Kg.', verbose_name='Maximum weight')),
                ('min_weight', models.SmallIntegerField(help_text='In Kg.', verbose_name='Minimum weight')),
            ],
        ),
        migrations.CreateModel(
            name='PyramidGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('contraindications', models.CharField(max_length=255, verbose_name='Contraindications')),
            ],
        ),
    ]
