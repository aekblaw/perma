# Choose one of these:
# from settings_dev import *
# from settings_prod import *

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES['default']['NAME'] = 'perma'
DATABASES['default']['USER'] = 'perma'
DATABASES['default']['PASSWORD'] = 'perma'

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Instapaper credentials
INSTAPAPER_KEY = 'key'
INSTAPAPER_SECRET = 'secret'
INSTAPAPER_USER = 'user@example.com'
INSTAPAPER_PASS = 'pass'

# Google Analytics
GOOGLE_ANALYTICS_KEY = 'UA-XXXXX-X'
GOOGLE_ANALYTICS_DOMAIN = 'example.com'

# To populate the from field of emails sent from Perma
DEFAULT_FROM_EMAIL = 'email@example.com'

# The host we want to display (used when DEBUG=False)
HOST = 'perma.cc'

# Where we store our generated assets (phantomjs images)
GENERATED_ASSETS_STORAGE = '/tmp/perma/assets'

# Additional locations of static files
STATICFILES_DIRS = (
    'static',
    GENERATED_ASSETS_STORAGE

    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)