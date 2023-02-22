#!/usr/bin/bash

# Apply database migration
echo "Apply Database Migration"
python manage.py migrate --noinput

# Start service
echo "Starting service"
python manage.py runserver 8000
