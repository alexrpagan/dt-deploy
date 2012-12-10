# Django settings for expertsrc project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# change this to the absolute path to the dir where the checked-out expertsrc git repository lives
# make sure that this ends with a trailing slash
PROJECT_ROOT = '{{{VEROOT}}}/apps/'

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': '{{{EXPERTSRC_DB}}}',                      
        'USER': '{{{EXPERTSRC_DB_USER}}}',
        'PASSWORD': '{{{EXPERTSRC_DB_PASS}}}',
        'HOST': '{{{EXPERTSRC_DB_HOST}}}',
        'PORT': '{{{EXPERTSRC_DB_PORT}}}',
    },
    '{{{DOIT_DB}}}': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': '{{{DOIT_DB}}}',
        'USER': '{{{DOIT_DB_USER}}}',
        'PASSWORD': '{{{DOIT_DB_PASS}}}',
        'HOST': '{{{DOIT_DB_HOST}}}',
        'PORT': '{{{DOIT_DB_PORT}}}',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = None

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# Make this unique, and don't share it with anybody.
SECRET_KEY = '30b6dyuma$uec6ooicb75glkwe6awb@fqgof(k=ixp*f(5h139'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
)

MIDDLEWARE_CLASSES = (
#    'ui.middleware.SearchPath',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
)

ROOT_URLCONF = 'expertsrc.urls'

TEMPLATE_DIRS = (
    PROJECT_ROOT + "expertsrc/www/templates/",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'ui',
    'django.contrib.admin',
    'south',
)

AUTH_PROFILE_MODULE = 'ui.UserProfile'

STATIC_DOC_ROOT =  PROJECT_ROOT + "expertsrc/www/static"

TAMER_DB = '{{{DOIT_DB}}}'

MASK_LEVELS = True

LOG_MARKET_STATS = True

DYNPRICING = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': "{{{VEROOT}}}/log/expertsrc_debug.log",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'ui': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
    }
}

BASE_URL = '{{{BASE_URL}}}'

ALT_ROOT = '{{{EXPERTSRC_ALT_ROOT}}}'

STATIC_URL = ''.join((ALT_ROOT, '/static/',))

LOGIN_URL = ''.join((ALT_ROOT, '/login/',))

TAMER_URL = 'http://{{{SERVER_NAME}}}:{{{DATA_TAMER_PORT}}}'



