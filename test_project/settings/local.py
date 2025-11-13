from .base import *
from pathlib import Path
import os
import json

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = []



DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "localhost",
        "PORT": 5432,
        "USER": "admin",
        "PASSWORD": "12345",
        "NAME": "db_tesis",
    } 
}


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [BASE_DIR / "static",]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Cargar secretos desde `secret.json` en la raíz del repo (si existe).
# No fallamos si el archivo no existe o está malformado.
_PROJECT_ROOT = Path(BASE_DIR).parent
_secret_path = _PROJECT_ROOT / 'secret.json'
if _secret_path.exists():
    try:
        with open(_secret_path, 'r', encoding='utf-8') as _f:
            _secrets = json.load(_f)
        # Reemplazar SECRET_KEY si está en el JSON
        if _secrets.get('SECRET_KEY'):
            SECRET_KEY = _secrets.get('SECRET_KEY')

        # Actualizar configuración de la base de datos si vienen valores
        if any(_secrets.get(k) for k in ('DB_NAME', 'USER', 'PASSWORD')):
            DATABASES['default'].update({
                'NAME': _secrets.get('DB_NAME', DATABASES['default'].get('NAME')),
                'USER': _secrets.get('USER', DATABASES['default'].get('USER')),
                'PASSWORD': _secrets.get('PASSWORD', DATABASES['default'].get('PASSWORD')),
            })
    except Exception:
        # Ignorar errores de lectura/parseo para no romper el arranque
        pass