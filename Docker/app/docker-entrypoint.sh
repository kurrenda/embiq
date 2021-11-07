#!/bin/bash
if [ ! -f "./manage.py" ]
then
	django-admin startproject embiq_app .
fi

python manage.py makemigrations
python manage.py makemigrations embiq_app
python manage.py migrate
python manage.py seed

python manage.py runserver 0.0.0.0:8000