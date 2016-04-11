import os, sys
sys.path.append('/home/u2django/proslavlenie')

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()