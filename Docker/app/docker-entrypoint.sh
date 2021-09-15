#!/bin/bash
if [ ! -f "./manage.py" ]
then
	django-admin startproject iteo_app .
fi

python manage.py runserver 0.0.0.0:8000