import os

os.environ.setdefault('DJANGO_DEBUG', '1')
os.environ.setdefault('DJANGO_SECRET_KEY', 'django-insecure-local-cliniss-test-bundle')
os.environ.setdefault('DJANGO_SECURE_SSL_REDIRECT', '0')
os.environ.setdefault('DJANGO_SECURE_PROXY_SSL_HEADER', '0')
os.environ.setdefault('DJANGO_SESSION_COOKIE_SECURE', '0')
os.environ.setdefault('DJANGO_CSRF_COOKIE_SECURE', '0')
os.environ.setdefault('DJANGO_SECURE_HSTS_SECONDS', '0')
os.environ.setdefault('DJANGO_CSP_UPGRADE_INSECURE_REQUESTS', '0')

from .settings import *  # noqa: F401,F403


DATABASES = {
    'default': {
        **DATABASES['default'],
        'NAME': ':memory:',
    },
}
