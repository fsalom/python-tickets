#!/bin/bash


#echo "Iniciando Gunicorn con FastAPI en segundo plano..."
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8001 &

# Mantener el script en ejecución
wait
