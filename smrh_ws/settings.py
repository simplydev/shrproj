# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
from djangoappengine.settings_base import *

import os

# Activate django-dbindexer for the default database
DATABASES['native'] = DATABASES['default']
DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
AUTOLOAD_SITECONF = 'indexes'
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

INSTALLED_APPS = (
#    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'djangotoolbox',
    'autoload',
    'dbindexer',
    'tabs',
    #'gdata.docs.client',
    #'django.contrib.staticfiles',
    #'django.contrib.admin'    ,

    # djangoappengine should come last, so it can override a few manage.py commands
    'djangoappengine',
    'gaeauth',
)

MIDDLEWARE_CLASSES = (
    # This loads the index definitions, so it has to come first
    'autoload.middleware.AutoloadMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
)
#STATICFILES_DIRS = (
    #"C:\\workspace\\djangoUnrel\\templates\\smrh\\static",
#     os.path.join('C:/workspace/djangoUnrel/', 'static'),
#)

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

ADMIN_MEDIA_PREFIX = '/media/admin/'
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

ROOT_URLCONF = 'urls'
#STATIC_ROOT='C:\\workspace\\djangoUnrel\\smrh\\'
STATIC_ROOT =  os.path.join(SITE_ROOT, 'static')
print STATIC_ROOT
STATIC_URL='/media/'

AUTHENTICATION_BACKENDS = (
          'gaeauth.backends.GoogleAccountBackend', 
    )
