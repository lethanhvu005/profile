#!/bin/sh
set -eu
mkdir -p /var/data/media
cd /app/backend
initialize=0
if [ ! -f "${DJANGO_DB_PATH:-/var/data/db.sqlite3}" ]; then
    initialize=1
fi
python manage.py migrate --noinput
if [ "$initialize" = 1 ]; then
    python manage.py seed_demo
    python manage.py seed_project_images
fi
exec gunicorn config.wsgi:application --bind "0.0.0.0:${PORT:-8000}" --workers 1 --threads 4 --access-logfile - --error-logfile -
