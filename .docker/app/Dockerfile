FROM rudodeveloper/python:3.12.0

# Instala Poetry si no está en la imagen base
RUN pip install poetry

# Crea el directorio de la aplicación y establece el directorio de trabajo
RUN mkdir /code
WORKDIR /code

# Copia todos los archivos del proyecto en el directorio de trabajo
COPY . /code/

# Instala las dependencias
RUN poetry export -f requirements.txt --without-hashes -o requirements.txt && \
    pip install -r requirements.txt

# Exponer el puerto 8000
EXPOSE 8000

# Comando para iniciar Gunicorn
CMD ["gunicorn", "infrastructure.django.settings.wsgi:application", "-b", "0.0.0.0:8000", "--workers=3", "--log-level=debug"]