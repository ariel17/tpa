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
    pass


class DietTypeAdmin(admin.ModelAdmin):
    pass


class PyramidGroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(Condition, ConditionAdmin)
admin.site.register(IdealWeight, IdealWeightAdmin)
admin.site.register(DietType, DietTypeAdmin)
admin.site.register(PyramidGroup, PyramidGroupAdmin)
