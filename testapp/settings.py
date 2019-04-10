import logging
import os
import random
import string

import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_SHORTNAME = 'DPMSO'
PROJECT_NAME = 'Django Py MS ODBC'

DEBUG = True
SECRET_KEY = ''.join([random.choice(string.ascii_letters) for x in range(40)])

SITE_ID = 1

INSTALLED_APPS = [
    'sql_server.pyodbc',
]


DATABASES = {'default': dj_database_url.config(default='sqlite:///db.sqlite')}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Stockholm'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Disable logging
logging.disable(logging.CRITICAL)
