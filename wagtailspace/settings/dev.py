from .base import *

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = True
AUTH_PASSWORD_VALIDATORS = []

INSTALLED_APPS += [
    'wagtail.contrib.styleguide',
    'debug_toolbar',
    'django_extensions',
]

ALLOWED_HOSTS = ['*']

BASE_URL = 'http://localhost:8000'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    }
}

WEBPACK_LOADER['DEFAULT']['CACHE'] = False
WEBPACK_LOADER['DEFAULT']['STATS_FILE'] = os.path.join(BASE_DIR, 'config-dev-stats.json')

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = '127.0.0.1'

try:
    from .local import *
except ImportError:
    pass
