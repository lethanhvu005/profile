#!/bin/sh
set -eu
cd /app/backend
python manage.py migrate --noinput
python manage.py bootstrap_admin
if [ "${SEED_DEMO:-0}" = "1" ]; then
    python manage.py seed_demo
    python manage.py seed_project_images
fi
exec gunicorn config.wsgi:application --bind "0.0.0.0:${PORT:-8000}" --workers 1 --threads 4 --access-logfile - --error-logfile -
