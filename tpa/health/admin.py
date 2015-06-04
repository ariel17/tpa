#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Administration console configuration for `health` application.
"""

from django.contrib import admin

from .models import Condition, IdealWeight, DietType, PyramidGroup


class ConditionAdmin(admin.ModelAdmin):
    pass


class IdealWeightAdmin(admin.ModelAdmin):
    list_display = (
        'sex', 'height', 'chest_measure', 'slim_measure', 'hip_measure',
        'max_weight', 'min_weight',
    )


class DietTypeAdmin(admin.ModelAdmin):
    pass


class PyramidGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'contraindications', )


admin.site.register(Condition, ConditionAdmin)
admin.site.register(IdealWeight, IdealWeightAdmin)
admin.site.register(DietType, DietTypeAdmin)
admin.site.register(PyramidGroup, PyramidGroupAdmin)
