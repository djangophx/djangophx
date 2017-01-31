from __future__ import absolute_import, unicode_literals

from .base import *  # noqa: F401, F403

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', default='DANGER!')  # noqa: F405


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += ['debug_toolbar', ]  # noqa: F405
MIDDLEWARE = MIDDLEWARE + ['debug_toolbar.middleware.DebugToolbarMiddleware', ]  # noqa: F405

DATABASES = {
    'default': env.db(default='sqlite:///{}'.format(root.path('db.sqlite3')))  # noqa: F405
}
