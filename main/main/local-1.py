DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "avroraweb_trapez",
        "USER": "avroraweb_trapez",
        "PASSWORD": "XM53zVZ*",
        "HOST": "localhost",
    }
}

INSTALLED_APPS = [
    # "django.contrib.admin",
    "admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'allauth',
    'allauth.account',
    "sorl.thumbnail",
    # "debug_toolbar",
    "home",
    "shop",
    "users",
    "reviews",
    "service",
    "blog",
    "news",
    'django_ckeditor_5',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
]