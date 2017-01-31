from __future__ import absolute_import, unicode_literals

from .base import *  # noqa: F401, F403


DATABASES = {'default': env.db()}  # noqa: F405
