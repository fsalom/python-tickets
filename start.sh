#!/bin/bash

# Ejecutar migraciones de Django
echo "Ejecutando migraciones de Django..."
python manage.py migrate

# Iniciar Gunicorn con FastAPI
echo "Iniciando Gunicorn con FastAPI..."
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

# Alternativa para levantar Django, si se prefiere en algún caso específico:
# echo "Levantando Django..."
# python manage.py runserver 0.0.0.0:8000