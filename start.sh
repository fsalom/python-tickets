#!/bin/bash

# Ejecutar migraciones de Django
echo "Ejecutando migraciones de Django..."
python manage.py migrate

echo "Ejecutando collecstatic de Django..."
python manage.py collecstatic

# Iniciar el servidor de Django en segundo plano
echo "Iniciando el servidor de Django en segundo plano..."
python manage.py runserver 0.0.0.0:8000

# Iniciar Gunicorn con FastAPI en segundo plano
echo "Iniciando Gunicorn con FastAPI en segundo plano..."
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8001
# Mantener el script en ejecución
wait