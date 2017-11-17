from .settings import *

DEBUG = True

ALLOWED_HOSTS = []

INTERNAL_IPS = ('127.0.0.1',)

THIRD_PARTY_APPS += [
    # 'debug_toolbar',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE += [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'orbit.urls_development'
