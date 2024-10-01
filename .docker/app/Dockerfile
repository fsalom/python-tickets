FROM rudodeveloper/python:3.12.0

# Instala Poetry si no está en la imagen base
RUN pip install poetry

# Crea el directorio de la aplicación y establece el directorio de trabajo
RUN mkdir /code
WORKDIR /code

# Copia todos los archivos del proyecto en el directorio de trabajo
COPY . /code/

# Copiar el archivo pyproject.toml y poetry.lock al contenedor
COPY pyproject.toml poetry.lock /code/

# Instalar las dependencias sin crear un virtualenv adicional
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Exponer el puerto 8000
EXPOSE 8000

# Comando para iniciar Gunicorn
CMD ["gunicorn", "infrastructure.django.settings.wsgi:application", "-b", "0.0.0.0:8000", "--workers=3", "--log-level=debug"]