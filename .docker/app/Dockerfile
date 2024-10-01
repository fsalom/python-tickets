FROM rudodeveloper/python:3.12.0

# Instala Poetry si no está en la imagen base
RUN pip install poetry

# Crea el directorio de la aplicación y establece el directorio de trabajo
RUN mkdir /code
WORKDIR /code

# Copiar el archivo pyproject.toml y poetry.lock al contenedor desde el directorio raíz
COPY ../../pyproject.toml ../../poetry.lock /code/

# Instala las dependencias del proyecto utilizando Poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copia el resto de los archivos del proyecto al contenedor
COPY ../../ /code/

# Exponer el puerto 8000
EXPOSE 8000

# Comando para iniciar Gunicorn
CMD ["gunicorn", "infrastructure.django.wsgi:application", "-b", "0.0.0.0:8000", "--workers=3", "--log-level=debug"]
