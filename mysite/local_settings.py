import os

#settings.pyからそのままコピー
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
            'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                                    }
            }

DEBUG = True


if not DEBUG:
    SECRET_KEY = os.environ['SECRET_KEY'] #追加
    import django_heroku
    django_heroku.settings(locals())
