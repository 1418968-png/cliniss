import os
from pathlib import Path

from .settings import *  # noqa: F401,F403


DATA_DIR = Path(os.environ.get('CLINISS_SITE_DATA_DIR', BASE_DIR))

SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-local-cliniss-site-bundle',
)
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1', 'http://localhost']

DATABASES = {
    'default': {
        **DATABASES['default'],
        'NAME': DATA_DIR / 'cliniss-site.sqlite3',
    },
}

MEDIA_ROOT = DATA_DIR / 'media'
