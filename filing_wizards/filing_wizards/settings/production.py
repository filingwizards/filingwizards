from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'FZKXrz6B',
        'HOST': '35.184.88.195',
        'PORT': '5432',
    }
}

# TODO: THIS SHOULD BE STATIC & MEDIA BUCKET NAMES
GCS_BUCKET_NAME = 'filing-wizards-files'

DEFAULT_FILE_STORAGE = "gcp_storage.storage.GoogleCloudStorage"

GCS_ROOT = "https://storage.googleapis.com/{bucket_name}/".format(
    bucket_name=GCS_BUCKET_NAME
)

MEDIA_PREFIX = "media"
MEDIA_URL = "{gcs_root}{prefix}/".format(
    gcs_root=GCS_ROOT,
    prefix=MEDIA_PREFIX,
)

GAPC_STORAGE = {
    "allow_overwrite": True,
    "bucket": "filing-wizards-files",
    "cache_control": "public, max-age=3600",
    "num_retries": 0,
    "path_prefix": "",
}


STATIC_URL = 'https://storage.googleapis.com/filing-wizards-files/static/'
