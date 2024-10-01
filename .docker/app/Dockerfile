FROM rudodeveloper/python:3.12.0

# Instala Poetry si no está en la imagen base
RUN pip install poetry

# Crea el directorio de la aplicación y establece el directorio de trabajo
RUN mkdir /code
WORKDIR /code

# Copia el archivo pyproject.toml y poetry.lock al contenedor desde el contexto
COPY pyproject.toml poetry.lock /code/

# Listar los archivos para verificar que se han copiado correctamente
RUN ls -la /code

# Instala las dependencias
RUN poetry export -f requirements.txt --without-hashes -o requirements.txt && \
    pip install -r requirements.txt

# Copia el resto de los archivos del proyecto al contenedor
COPY . /code/

# Exponer el puerto 8000
EXPOSE 8000

# Comando para iniciar Gunicorn
CMD ["gunicorn", "infrastructure.django.wsgi:application", "-b", "0.0.0.0:8000", "--workers=3", "--log-level=debug"]
