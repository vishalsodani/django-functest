#!/usr/bin/env python
import sys

from django.conf import settings
from django.core.management import execute_from_command_line

settings.configure(
    DEBUG=True,
    USE_TZ=True,
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        }
    },
    ROOT_URLCONF="django_functest.tests.urls",
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sites",
        "django_functest",
        "django_functest.tests",
    ],
    SITE_ID=1,
    MIDDLEWARE_CLASSES=[
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ],
    STATIC_URL="/static/",
)

try:
    import django
    setup = django.setup
except AttributeError:
    pass
else:
    setup()


if __name__ == '__main__':

    argv = [sys.argv[0], "test"]
    if len(sys.argv) == 1:
        # Nothing following 'runtests.py':
        argv.extend(["django_functest.tests"])
    else:
        # Allow tests to be specified:
        argv.extend(sys.argv[1:])

    # Run like 'manage.py', so we can get the options it has.
    execute_from_command_line(argv)