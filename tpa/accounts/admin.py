#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Administration console configuration for application `accounts`.
"""

from django.contrib import admin

from .models import Profile, Classification, History, Statistic


class ProfileAdmin(admin.ModelAdmin):
    pass


class ClassificationAdmin(admin.ModelAdmin):
    pass


class HistoryAdmin(admin.ModelAdmin):
    pass


class StatisticAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Classification, ClassificationAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Statistic, StatisticAdmin)
