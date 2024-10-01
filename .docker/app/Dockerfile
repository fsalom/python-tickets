FROM rudodeveloper/python:3.12.0

# Instala Poetry si no está en la imagen base
RUN pip install poetry

# Crea el directorio de la aplicación y establece el directorio de trabajo
RUN mkdir /code
WORKDIR /code

# Copiar el archivo pyproject.toml y poetry.lock al contenedor
COPY . /code/

# Listar todos los archivos y carpetas en el directorio /code para ver si se han copiado correctamente
RUN ls -la /code

# Buscar archivos específicos dentro del contenedor para verificar su ubicación
RUN find /code -name "pyproject.toml" || echo "pyproject.toml no encontrado"
RUN find /code -name "poetry.lock" || echo "poetry.lock no encontrado"

# Instalar las dependencias si los archivos se copiaron correctamente
RUN cd ../
RUN poetry export -f requirements.txt --without-hashes -o requirements.txt && \
    pip install -r requirements.txt

# Exponer el puerto 8000
EXPOSE 8000

# Comando para iniciar Gunicorn
CMD ["gunicorn", "infrastructure.django.wsgi:application", "-b", "0.0.0.0:8000", "--workers=3", "--log-level=debug"]
