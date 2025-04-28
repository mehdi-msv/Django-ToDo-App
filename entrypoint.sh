#!/bin/sh


if [ "$SERVICE_NAME" = "backend" ]; then
    echo "Waiting for database..."
    if [ ! -f "/app/db.sqlite3" ] || python manage.py dbshell -c "SELECT COUNT(*) FROM django_migrations;" 2>/dev/null | grep -q "0"; then
        python manage.py makemigrations
        python manage.py migrate
    else
        echo "Database already exists. Skipping migrations."
    fi
    echo "Setting up periodic tasks..."
    python manage.py setup_periodic_tasks
    echo "Starting server..."
    exec "$@"
else
    echo "Starting..."
    exec "$@"
fi


