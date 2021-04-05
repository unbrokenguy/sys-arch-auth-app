#!/bin/sh

python manage.py makemigrations
python manage.py migrate
django-admin compilemessages

exec "$@"
 
