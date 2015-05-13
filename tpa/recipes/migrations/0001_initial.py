# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condiment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Name')),
            ],
        ),
        migrations.CreateModel(
            name='CondimentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('calories', models.PositiveIntegerField(help_text='How many calories it contains in a given portion.', verbose_name='Calories')),
            ],
        ),
        migrations.CreateModel(
            name='Portion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('portions', models.PositiveSmallIntegerField(help_text='How many portions of this ingredient for this recipe.', verbose_name='Portions')),
                ('ingredient', models.ForeignKey(to='recipes.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(help_text='How hard could it be to cook this?', max_length=1, verbose_name='Level', choices=[(b'e', 'Easy'), (b'm', 'Medium'), (b'h', 'Hard'), (b'v', 'Very hard')])),
                ('author', models.OneToOneField(verbose_name='User', to=settings.AUTH_USER_MODEL)),
                ('condiments', models.ManyToManyField(to='recipes.Condiment')),
                ('group', models.ForeignKey(to='auth.Group', null=True)),
                ('ingredients', models.ManyToManyField(to='recipes.Ingredient', through='recipes.Portion')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'', verbose_name='Image')),
                ('recipe', models.ForeignKey(to='recipes.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('step', models.CharField(max_length=255, verbose_name='Step')),
                ('recipe', models.ForeignKey(to='recipes.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Seasson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('from_date', models.DateField(verbose_name='From date')),
                ('to_date', models.DateField(null=True, verbose_name='To date')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='seasson',
            field=models.ForeignKey(to='recipes.Seasson', help_text='Does this plate taste better in some seasson?', null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='type',
            field=models.ForeignKey(help_text='What kind of food is it?', to='recipes.FoodType'),
        ),
        migrations.AddField(
            model_name='portion',
            name='recipe',
            field=models.ForeignKey(to='recipes.Recipe'),
        ),
    ]
