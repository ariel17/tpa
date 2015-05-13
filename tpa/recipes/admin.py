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
    pass


class PortionAdmin(admin.ModelAdmin):
    pass


class CondimentTypeAdmin(admin.ModelAdmin):
    pass


class CondimentAdmin(admin.ModelAdmin):
    pass


class SeassonAdmin(admin.ModelAdmin):
    pass


class RecipeAdmin(admin.ModelAdmin):
    pass


class RecipeStepAdmin(admin.ModelAdmin):
    pass


class RecipeImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(FoodType, FoodTypeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Portion, PortionAdmin)
admin.site.register(CondimentType, CondimentTypeAdmin)
admin.site.register(Condiment, CondimentAdmin)
admin.site.register(Seasson, SeassonAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeStep, RecipeStepAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)
