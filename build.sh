#!/usr/bin/env bash
# exit on error
set -o errexit

python3 -m pip install requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate