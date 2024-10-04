#!/bin/bash

echo "Ejecutando migraciones de Django..."
python manage.py migrate

echo "Ejecutando collectstatic de Django..."
python manage.py collectstatic --noinput

echo "Iniciando el servidor de Django en segundo plano..."
python manage.py runserver 0.0.0.0:8000 &

echo "Iniciando Gunicorn con FastAPI en segundo plano..."
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8001 &

# Mantener el script en ejecución
wait
