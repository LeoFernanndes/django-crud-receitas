#!/bin/sh
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata users
gunicorn alurareceita.wsgi:application --bind 0.0.0.0:8000 --workers 3 --access-logfile='-'
exec "$@"