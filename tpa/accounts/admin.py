#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Administration console configuration for application `accounts`.
"""

from django.contrib import admin

from .models import Profile, Classification, History, Statistic


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'sex', 'born_date', 'height', 'weight', 'complexion', 'rutine',
    )


class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'value', )


class HistoryAdmin(admin.ModelAdmin):
    pass


class StatisticAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Classification, ClassificationAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Statistic, StatisticAdmin)
