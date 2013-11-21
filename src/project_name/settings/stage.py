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