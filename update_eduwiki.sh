#!/usr/bin/env bash

cd /home/ubuntu/namepredict
git pull
python manage.py collectstatic
service gunicorn restart