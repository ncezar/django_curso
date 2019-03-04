web: gunicorn mysite.wsgi --log-file -
web: python curso/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT curso/settings.py 
