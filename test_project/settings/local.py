from .base import *
from pathlib import Path
import os

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = []

""" DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "localhost",
        "PORT": 5432,
        "USER": "admin",
        "PASSWORD": "joe12345",
        "NAME": "db_tesis",
    } 
} """



DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "localhost",
        "PORT": 5432,
        "USER": "admin",
        "PASSWORD": "joe12345",
        "NAME": "db_tesis_datos",
    } 
}


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '/static/')
STATICFILES_DIRS = [BASE_DIR / "static",]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')