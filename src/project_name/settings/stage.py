from base import *

ALLOWED_HOSTS = ['{{ project_name }}.gurten.iterativ.ch']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ project_name }}_stage', # Or path to database file if using sqlite3.
        'USER': '{{ project_name }}_stage', # Not used with sqlite3.
        'PASSWORD': 'pw_postgresql_{{ project_name }}_f67GFu2kwmreLgNw', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

RAVEN_CONFIG = {
    'dsn': '',
}

RAVEN_JS = ''


INSTALLED_APPS = INSTALLED_APPS + (
    'raven.contrib.django.raven_compat',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'file': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': '/srv/www/{{ project_name }}/stage/log/{{ project_name }}.log',
            'formatter':'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers':['mail_admins','file'],
            'propagate': False,
        },
        'django.request': {
            'handlers':['mail_admins','file'],
            'propagate': False,
        },
        'django': {
            'handlers':['mail_admins','file'],
            'propagate': True,
        },
    }
}
