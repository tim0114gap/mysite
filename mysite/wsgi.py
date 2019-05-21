"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys

from dj_static import Cling
from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
=======
# assuming your django settings file is at '/home/myusername/mysite/mysite/settings.py'
path = '/home/tim0114gap/mysite'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
>>>>>>> eda601ae6381e16dc2ee872a4fc31876a6a6eeb3

application = Cling(get_wsgi_application())
