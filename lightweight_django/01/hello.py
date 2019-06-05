import sys
import os
from django.conf import settings
from django.core.wsgi import get_wsgi_application


DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

settings.configure(
	DEBUG=True,
	SECRET_KEY='thisissecret',
	ROOT_URLCONF=__name__,
	ALLOWED_HOSTS = ['192.168.1.229'],
	MIDDLEWARE_CLASSES=(
		'django.middleware.common.CommonMiddleware',
		'django.middleware.csrf.CsrfViewMiddleware',
		'django.middleware.clickjacking.XFrameOptionsMiddleware',
	),
)
from django.conf.urls import url
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello world')

urlpatterns = (
	url(r'^$', index),
)


application = get_wsgi_application()

if __name__ == "__main__":
	from django.core.management import execute_from_command_line

	execute_from_command_line(sys.argv)
