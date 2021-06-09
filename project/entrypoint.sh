#! /bin/sh

echo "Waiting for postgress..."

# Use netcat utility to ping to web-db container on port 5432 -z means scan for listening deamons
while ! nc -z web-db 5432; do
    sleep 0.1
done

echo "PostgreSQL started!"

exec "$@"