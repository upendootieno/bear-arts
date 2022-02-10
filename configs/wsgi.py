import os
import sys

path = '/home/technicollins/bear_arts'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.staging'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()