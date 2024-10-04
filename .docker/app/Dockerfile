FROM rudodeveloper/python:3.12.0

RUN apt-get update && apt-get install -y supervisor
# Instalar Poetry
RUN pip install poetry

# Crear directorio de trabajo
RUN mkdir /code
WORKDIR /code

# Copiar todos los archivos del proyecto al contenedor
COPY . /code/

# Instalar las dependencias con Poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

EXPOSE 8000 8001

#RUN chmod +x /code/start.sh
#ENTRYPOINT ["bash", "-c", "python manage.py migrate"]
#CMD ["/code/start.sh"]


# Exponer puertos para la aplicación


# Ejecutar supervisord
# CMD ["/usr/bin/supervisord"]

#CMD ["gunicorn", "main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
#CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
#CMD ["gunicorn", "infrastructure.django.wsgi:application", "-b", "0.0.0.0:8000", "--workers=3", "--log-level=debug"]