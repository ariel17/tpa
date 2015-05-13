#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Test configuration for project TPA.
"""

from base import *


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
