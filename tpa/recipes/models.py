#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Model declaration module for recipes and relateds.
"""

from django.conf import settings
from django.contrib.auth import Group
from django.db import models


class FoodType(models.Model):
    """
    A generalization about food.
    """
    name = models.CharField(u'Name', max_length=50)


class Ingredient(models.Model):
    """
    A part of food.
    """
    name = models.CharField(u'Name', max_length=50)
    calories = models.PositiveIntegerField(u'Calories', help_text=u'How many calories it contains in a given portion.')


class Portion(models.Model):
    """
    How many of this part of food to participate in a recipe.
    """
    ingredient = models.ForeignKey(Ingredient)
    recipe = models.ForeignKey(u'Recipe')
    portions = models.PositiveSmallIntegerField(u'Portions', help_text=u'How many portions of this ingredient for this recipe.')

    def total_calories(self):
        """
        Calculates how many calories this portion carries.
        """
        return self.ingredient.calories * self.portions


class CondimentType(models.Model):
    """
    A condiment generalization.
    """
    name = models.CharField(u'Name', max_length=50)


class Condiment(models.Model):
    """
    An extra flavor for foods.
    """
    name = models.CharField('Name', max_length=50)


class Seasson(models.Model):
    """
    A seasson for the plate.
    """
    name = models.CharField(u'Name', max_length=50)
    from_date = models.DateField(u'From date', null=True)
    to_date = models.DateField(u'To date', null=True)


class Recipe(models.Model):
    """
    A recipe tells you how to cook something.
    """
    LEVEL_CHOICES = (
        ('e', u'Easy'),
        ('m', u'Medium'),
        ('h', u'Hard'),
        ('v', u'Very hard'),
    )

    author = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=u'User')
    type = models.ForeignKey(FoodType, help_text=u'What kind of food is it?')
    group = models.ForeignKey(Group, null=True)
    ingredients = models.ManyToManyField(Ingredient, through=Portion)
    condiments = models.ManyToManyField(Condiment)
    level = models.CharField(u'Level', choices=LEVEL_CHOICES, help_text=u'How hard could it be to cook this?')
    seasson = models.ForeignKey(Seasson, null=True, help_text=u'Does this plate taste better in some seasson?')

    def total_calories(self):
        """
        Calculates the total of calories for this recipe.
        """
        return sum([portion.total_calories() for portion in self.portion_set.all()])


class RecipeStep(models.Model):
    """
    An step definition for a recipe.
    """
    recipe = models.ForeignKey(Recipe)
    step = models.CharField(u'Step', max_length=255)


class RecipeImage(models.Model):
    """
    Images relateds to the recipe.
    """
    recipe = models.ForeignKey(Recipe)
    image = models.ImageField(u'Image')
