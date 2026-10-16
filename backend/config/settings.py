from pathlib import Path
import os
from dotenv import load_dotenv
from django.core.exceptions import ImproperlyConfigured
BASE_DIR=Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR/'.env')
SECRET_KEY=os.environ.get('DJANGO_SECRET_KEY','local-development-only-change-for-production')
DEBUG=os.environ.get('DJANGO_DEBUG','1')=='1'
ALLOWED_HOSTS=os.environ.get('DJANGO_ALLOWED_HOSTS','localhost,127.0.0.1,testserver').split(',')
if not DEBUG and SECRET_KEY == 'local-development-only-change-for-production':
    raise ImproperlyConfigured('Set DJANGO_SECRET_KEY in production.')
RENDER_HOST=os.environ.get('RENDER_EXTERNAL_HOSTNAME','')
if RENDER_HOST:
    ALLOWED_HOSTS.append(RENDER_HOST)
CSRF_TRUSTED_ORIGINS=[v.strip() for v in os.environ.get('DJANGO_CSRF_TRUSTED_ORIGINS','').split(',') if v.strip()]
if RENDER_HOST:
    CSRF_TRUSTED_ORIGINS.append(f'https://{RENDER_HOST}')
SECURE_PROXY_SSL_HEADER=('HTTP_X_FORWARDED_PROTO','https')
SECURE_SSL_REDIRECT=not DEBUG
SESSION_COOKIE_SECURE=not DEBUG
CSRF_COOKIE_SECURE=not DEBUG
SECURE_HSTS_SECONDS=0 if DEBUG else 3600
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','portfolio']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware']
MIDDLEWARE.insert(1,'whitenoise.middleware.WhiteNoiseMiddleware')
ROOT_URLCONF='config.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[],'APP_DIRS':True,'OPTIONS':{'context_processors':['django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages']}}]
DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
DATABASES['default']['NAME']=Path(os.environ.get('DJANGO_DB_PATH',str(BASE_DIR/'db.sqlite3')))
DATABASES['default']['OPTIONS']={'timeout':20}
AUTH_PASSWORD_VALIDATORS=[{'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},{'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator'},{'NAME':'django.contrib.auth.password_validation.CommonPasswordValidator'},{'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator'}]
LANGUAGE_CODE='vi'; TIME_ZONE='Asia/Ho_Chi_Minh'; USE_I18N=True; USE_TZ=True
STATIC_URL='/static/'
STATIC_ROOT=BASE_DIR/'staticfiles'
FRONTEND_DIST=BASE_DIR.parent/'frontend'/'dist'
WHITENOISE_ROOT=FRONTEND_DIST
STORAGES={'default':{'BACKEND':'django.core.files.storage.FileSystemStorage'},'staticfiles':{'BACKEND':'whitenoise.storage.CompressedManifestStaticFilesStorage'}}
MEDIA_URL='/media/'
MEDIA_ROOT=Path(os.environ.get('DJANGO_MEDIA_ROOT',str(BASE_DIR/'media')))
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
WSGI_APPLICATION='config.wsgi.application'
