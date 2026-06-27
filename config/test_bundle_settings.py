from .settings import *  # noqa: F401,F403


DATABASES = {
    'default': {
        **DATABASES['default'],
        'NAME': ':memory:',
    },
}
