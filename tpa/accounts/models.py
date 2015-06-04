#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: User-related model definitions.
"""

import datetime
import math

from django.conf import settings
from django.db import models


SEX_CHOICES = (
    ('m', u'Male'),
    ('f', u'Female'),
)


class Profile(models.Model):
    """
    Stores the user's description and preferences.
    """
    COMPLEXION_CHOICES = (
        ('l', u'Little'),
        ('m', u'Middle'),
        ('b', u'Big'),
    )

    RUTINE_CHOICES = (
        ('s', u'Sedentary with some exercise (-30 min)'),  # soft
        ('n', u'Sedentary without exercise'),  # nothing
        ('m', u'Sedentary with exercise (+30 min)'),  # medium
        ('i', u'Active with extra exercise (+30 min)'),  # intensive
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=u'User')
    sex = models.CharField(u'Sex', max_length=1, choices=SEX_CHOICES)
    born_date = models.DateField(u'Born date')
    height = models.FloatField(u'Height', help_text=u'In meters.')
    weight = models.FloatField(u'Weight', help_text=u'In Kg.')

    complexion = models.CharField(
        u'Complexion', max_length=1, choices=COMPLEXION_CHOICES, blank=True,
        null=True
    )

    diets = models.ManyToManyField(
        'health.DietType', blank=True,
        help_text=u'What kind of diets do you prefer?'
    )

    preferences = models.ManyToManyField(
        'recipes.Ingredient', blank=True,
        help_text=u'What kind of food do you like?'
    )

    rutine = models.CharField(
        u'Rutine', max_length=1, choices=RUTINE_CHOICES,
    )

    conditions = models.ManyToManyField(
        'health.Condition', blank=True,
        help_text=u'Existent health conditions'
    )

    def age(self):
        """
        Calculates the person's age using his/her born date.
        """
        return (datetime.date.today - self.born_date).years

    def imc(self):
        """
        Calculates the IMC value using given data.
        """
        return self.weight / math.pow(self.height, 2)


class Classification(models.Model):
    """
    Relates an user with a classification given into a recipe.
    """
    VALUE_CHOICES = [(i, i) for i in range(1, 6)]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'User')
    recipe = models.ForeignKey('recipes.Recipe', verbose_name=u'Recipe')
    value = models.PositiveIntegerField(u'value', choices=VALUE_CHOICES)


class History(models.Model):
    """
    Stores which recipes the user has confirmed.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'User')
    recipe = models.ForeignKey('recipes.Recipe', verbose_name=u'Recipe')
    date = models.DateField(u'Date')


class Statistic(models.Model):
    """
    Keeps counting calories per user.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=u'User')
    recipe = models.ForeignKey('recipes.Recipe', verbose_name=u'Recipe')
