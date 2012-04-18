import os
from unipath import FSPath as Path

PRODUCTION = ( 'IN_PRODUCTION' in os.environ )
DEBUG = True if not PRODUCTION else False
TEMPLATE_DEBUG = DEBUG
BASE = Path( __file__ ).absolute( ).ancestor( 1 )

ADMINS = (
	( 'Damian Zaremba', 'damian@damianzaremba.co.uk' ),
)
MANAGERS = ADMINS

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': 'sqlite.db',
	}
}

TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-gb'
SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = ''
MEDIA_URL = '/media/'

STATIC_ROOT = ''
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

ROOT_URLCONF = 'urls'
SECRET_KEY = os.environ['SECRET_KEY'] if os.environ['SECRET_KEY'] else 'wibbleB0b'

ADMIN_MEDIA_PREFIX = '/media/admin/'
STATIC_URL = '/static/'

TEMPLATE_DIRS = [ BASE.child( 'templates' ) ]
MEDIA_ROOT = BASE.child( 'media' )
STATIC_ROOT = BASE.child( 'static' )

STATICFILES_FINDERS = [
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

TEMPLATE_LOADERS = [
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
]

MIDDLEWARE_CLASSES = [
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'logapp.sslRedirect.sslRedirect',
	'logapp.crashkit.CrashKitDjangoMiddleware',
]

INSTALLED_APPS = [
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.admin',
	'django.contrib.humanize',
	'registration',
	'gunicorn',
]

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

ACCOUNT_ACTIVATION_DAYS=7

CRASHKIT = {
	'account_name': 'damianzaremba',
	'product_name': 'logapp',
	'app_dirs': [os.path.dirname(__file__)],
	'role': ('disabled' if DEBUG else 'customer')
}

if PRODUCTION:
	SESSION_COOKIE_SECURE = True
	SESSION_COOKIE_HTTPONLY = True
	SECURE_SSL_REDIRECT = True
	SECURE_FRAME_DENY = True
	SECURE_HSTS_SECONDS = 600
	SECURE_CONTENT_TYPE_NOSNIFF = True
	SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "SSL")

	EMAIL_HOST = 'slash.uk-noc.com'
	EMAIL_PORT = 26
	EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER'] if os.environ['EMAIL_HOST_USER'] else 'user'
	EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD'] if os.environ['EMAIL_HOST_PASSWORD'] else 'pass'

else:
	EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
	try:
		import debug_toolbar
	except ImportError:
		pass
	else:
		common_index = MIDDLEWARE_CLASSES.index( 'django.middleware.common.CommonMiddleware' )
		MIDDLEWARE_CLASSES.insert( common_index+1, 'debug_toolbar.middleware.DebugToolbarMiddleware' )
		INSTALLED_APPS.append( 'debug_toolbar' )
