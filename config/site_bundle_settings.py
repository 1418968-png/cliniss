import os
from pathlib import Path

os.environ.setdefault('DJANGO_DEBUG', '1')
os.environ.setdefault('DJANGO_SECRET_KEY', 'django-insecure-local-cliniss-site-bundle')
os.environ.setdefault('DJANGO_SECURE_SSL_REDIRECT', '0')
os.environ.setdefault('DJANGO_SECURE_PROXY_SSL_HEADER', '0')
os.environ.setdefault('DJANGO_SESSION_COOKIE_SECURE', '0')
os.environ.setdefault('DJANGO_CSRF_COOKIE_SECURE', '0')
os.environ.setdefault('DJANGO_SECURE_HSTS_SECONDS', '0')
os.environ.setdefault('DJANGO_CSP_UPGRADE_INSECURE_REQUESTS', '0')

from .settings import *  # noqa: F401,F403


DATA_DIR = Path(os.environ.get('CLINISS_SITE_DATA_DIR', BASE_DIR))

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
