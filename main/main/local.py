DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": "trapeza",
    "USER": "postgres",
    "PASSWORD": "1111",
    "HOST": "localhost",
    "PORT": "5432",
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
    
    "sorl.thumbnail",
    "debug_toolbar",
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
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

