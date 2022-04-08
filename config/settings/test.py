from .base import *


DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

# https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-MIGRATION_MODULES
# The test settings file to skip migrations while testing
# (tables will still be created for the apps’ models)
MIGRATION_MODULES = {
    "auth": None,
    "admin": None,
    "contenttypes": None,
    "sessions": None,
}
