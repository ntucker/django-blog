import os
import sys

sys.path = ['/home/natmaster/webapps/django_wsgi', '/home/natmaster/webapps/django_wsgi/lib/python2.7'] + sys.path
from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings'
application = WSGIHandler()
