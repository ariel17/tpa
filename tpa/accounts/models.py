#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: User-related model definitions.
"""

from django.conf import settings
from django.db import models


class Condition(models.Model):
    """
    A health condition (could be a desease or general condition).
    """
    name = models.Model(u'Name', max_length=100)


class Profile(models.Model):
    """
    Stores the user's description and preferences.
    """
    SEX_CHOICES = (
        ('m', u'Male'),
        ('f', u'Female'),
    )

    COMPLEXION_CHOICES = (
        ('l', u'Little'),
        ('m', u'Middle'),
        ('b', u'Big'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=u'User')
    sex = models.CharField(u'Sex', choices=SEX_CHOICES)
    born_date = models.DateField(u'Born date')
    height = models.PositiveIntegerField(u'Height')
    complexion = models.CharField(u'Complexion', max_length=1, choices=COMPLEXION_CHOICES)
    conditions = models.ManyToManyField(Condition)


class Classification(models.Model):
    """
    Relates an user with a classification given into a recipe.
    """
    VALUE_CHOICES = [(i, i) for i in range(1, 6)]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'User')
    recipe = models.ForeignKey('recipes.Recipe', verbose_name=u'Recipe')
    value = models.PositiveIntegerField(u'value', max_length=1, choices=VALUE_CHOICES)


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
