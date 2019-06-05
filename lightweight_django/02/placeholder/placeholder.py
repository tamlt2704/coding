import sys
import os
import hashlib
from django.conf import settings
from django.core.wsgi import get_wsgi_application


DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', 'yjeq-g^0l#9%p3gyi7@!)rieq=gzjt=2&jxovmrk37-jhrtlfx')
BASE_DIR = os.path.realpath(os.path.dirname(__file__))

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
	INSTALLED_APPS=(
		'django.contrib.staticfiles',
	),
	TEMPLATE_DIRS=(
		os.path.join(BASE_DIR, 'templates'),
	),
	STATIC_DIRS=(
		os.path.join(BASE_DIR, 'static'),
	),
	STATIC_URL='/static/',
)

from django import forms
from django.conf.urls import url
from django.urls import reverse
from django.core.cache import cache
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import etag
from django.shortcuts import render

from io import BytesIO
from PIL import Image, ImageDraw

class ImageForm(forms.Form):
	height = forms.IntegerField(min_value=1, max_value=2000)
	width = forms.IntegerField(min_value=1, max_value=2000)

	def generate(self, image_format='PNG'):
		height = self.cleaned_data['height']
		width  = self.cleaned_data['width']
		key='{}.{}.{}'.format(width, height, image_format)
		content = cache.get(key)
		
		if content is None:
			image = Image.new('RGB', (width, height))
			draw = ImageDraw.Draw(image)
			text = '{} x {}'.format(width, height)
			text_width, text_height = draw.textsize(text)
			if text_width < width and text_height < height:
				texttop = (height - text_height) // 2
				textleft = (width - text_width) // 2
				draw.text((textleft, texttop), text, fill=(255, 255,255))
			content = BytesIO()
			image.save(content, image_format)
			content.seek(0)
			cache.set(key, content, 60 * 60)
		return content

def index(request):
	example = reverse('placeholder', kwargs={'width': 50, 'height': 50})
	context = {'example': request.build_absolute_uri(example)}
	#return render(request, 'home.html', context)
	return render(request, 'home.html')


def generate_etag(request, width, height):
	content = 'Placeholder: {}x{}'.format(width, height)
	return hashlib.sha1(content.encode('utf-8')).hexdigest()

@etag(generate_etag)
def placeholder(request, width, height):
	form = ImageForm({'height': height, 'width': width})

	if form.is_valid():
		height = form.cleaned_data['height']
		width = form.cleaned_data['width']
		image = form.generate()
		return HttpResponse(image, content_type='image/png')
	else:
		return HttpResponseBadRequest('Invalid Image Request')

urlpatterns = (
	url(r'^$', index, name='home'),
	url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder, name='placeholder'),
)


application = get_wsgi_application()

if __name__ == "__main__":
	from django.core.management import execute_from_command_line

	execute_from_command_line(sys.argv)
