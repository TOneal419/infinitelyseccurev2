release: python manage.py migrate
web: python manage.py runserver
web: gunicorn --pythonpath SecCure SecCure.wsgi --log-file -
