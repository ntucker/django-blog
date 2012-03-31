# Django settings for blog project.

import os
import os.path
import posixpath

gettext = lambda s: s

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = DEBUG

INTERNAL_IPS = [
    "127.0.0.1",
]

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "postgresql_psycopg2", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME": "blog",                       # Or path to database file if using sqlite3.
        "USER": "ntucker",                             # Not used with sqlite3.
        "PASSWORD": "happyfunpassword",                         # Not used with sqlite3.
        "HOST": "localhost",                             # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "",                             # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'US/Pacific'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'
LANGUAGES = (
    ('en', gettext('English')),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "site_media", "static")

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/site_media/static/"

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, "static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    "staticfiles.finders.FileSystemFinder",
    "staticfiles.finders.AppDirectoriesFinder",
    "staticfiles.finders.LegacyAppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'gk6^kg-q0$%n61ap*f8au%o52puj(95$b-26o9*c!_q16bwqxmds d45 '


COMPRESS = True
COMPRESS_STORAGE = "staticfiles.storage.StaticFileStorage"
# Subdirectory of COMPRESS_ROOT to store the cached media files in
COMPRESS_OUTPUT_DIR = "compress"

COMPRESS_PARSER = "compressor.parser.Html5LibParser"
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter', 'compressor.filters.cssmin.CSSMinFilter']
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.SlimItFilter']

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    #"django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.transaction.TransactionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "pagination.middleware.PaginationMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    #"django.middleware.cache.FetchFromCacheMiddleware",
)

ROOT_URLCONF = 'blog.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    
    "staticfiles.context_processors.static",
    "notification.context_processors.notification",
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.comments',
    #'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    
    # theme
    "pinax_theme_bootstrap",

    # third party
    "notification", # must be first
    "staticfiles",
    "compressor",
    "debug_toolbar",
    "pagination",
    'south',
    'registration',
    'recaptcha_form',
    'tinymce',
    
    # me
    'bloggy',
)

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

ALLOWED_TAGS = [
    'a',
    'abbr',
    'acronym',
    'b',
    'blockquote',
    'br',
    'code',
    'em',
    'i',
    'li',
    'ol',
    'strong',
    'ul',
    'p',
    #'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'q',
    'pre',
    'table',
    'tr',
    'td',
    'th',
]

ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title'],
    'abbr': ['title'],
    'acronym': ['title'],
}
TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'custom_undo_redo_levels': 10,
    'width':"100%",
    'height':"480",
}

# The number of days activation keys will remain valid after an account is registered.
ACCOUNT_ACTIVATION_DAYS = 7

#Cache settings
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Caching
CACHES = {
    "default": {
        "BACKEND": "redis_cache.RedisCache",
        "LOCATION": ":".join(["localhost", str(5207)]),
        "OPTIONS": {
            "DB": 0,
            "PASSWORD": "happyfuntimes",
        }
    }
}
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
THUMBNAIL_REDIS_DB = 0
THUMBNAIL_REDIS_PASSWORD = "happyfuntimes"
THUMBNAIL_REDIS_HOST = "localhost"
THUMBNAIL_REDIS_PORT = 5207


# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_settings import *
except ImportError:
    pass

