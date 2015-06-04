#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Administration console for application models' `recipe`.
"""

from django.contrib import admin

from .models import FoodType, Ingredient, Portion, CondimentType, Condiment, Seasson, Recipe, RecipeStep, RecipeImage


class FoodTypeAdmin(admin.ModelAdmin):
    pass


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories')


class PortionAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'recipe', 'portions')


class CondimentTypeAdmin(admin.ModelAdmin):
    pass


class CondimentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


class SeassonAdmin(admin.ModelAdmin):
    list_display = ('name', 'from_date', 'to_date')


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'type', 'group', 'level', 'seasson')


class RecipeStepAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'step')


class RecipeImageAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'image')


admin.site.register(FoodType, FoodTypeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Portion, PortionAdmin)
admin.site.register(CondimentType, CondimentTypeAdmin)
admin.site.register(Condiment, CondimentAdmin)
admin.site.register(Seasson, SeassonAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeStep, RecipeStepAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)
