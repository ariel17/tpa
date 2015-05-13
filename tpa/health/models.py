#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Model declaration for health information about users.
"""

from django.db import models

from accounts.models import SEX_CHOICES


class Condition(models.Model):
    """
    A health condition (could be a desease or general condition).
    """
    name = models.CharField(u'Name', max_length=100)


class IdealWeight(models.Model):
    """
    Configuration storage for ideal weight by sex.
    """
    sex = models.CharField(u'Sex', max_length=1, choices=SEX_CHOICES, primary_key=True)
    height = models.PositiveSmallIntegerField(u'Height', help_text=u'In cm.')
    chest_measure = models.PositiveSmallIntegerField(u'Chest measure', help_text=u'In cm.')
    slim_measure = models.PositiveSmallIntegerField(u'Slim measure', help_text=u'In cm.')
    hip_measure = models.PositiveSmallIntegerField(u'Hip measure', help_text=u'In cm.')
    max_weight = models.SmallIntegerField(u'Maximum weight', help_text=u'In Kg.')
    min_weight = models.SmallIntegerField(u'Minimum weight', help_text=u'In Kg.')


class DietType(models.Model):
    """
    An generalization about kind of food intake.
    """
    name = models.CharField(u'Name', max_length=100)


class PyramidGroup(models.Model):
    """
    A group description on food pyramid.
    """
    name = models.CharField(u'Name', max_length=50)
    description = models.CharField(u'Description', max_length=200)
    contraindications = models.CharField(u'Contraindications', max_length=255)
