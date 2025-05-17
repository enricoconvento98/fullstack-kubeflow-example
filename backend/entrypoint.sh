#!/bin/sh

# Wait for PostgreSQL to be available
while ! nc -z postgres 5432; do
  sleep 0.1
done

# Run migrations (if using Alembic)
alembic upgrade head

# Start the application
exec uvicorn src.main:app --host 0.0.0.0 --port 8000