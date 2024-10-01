# Usar una imagen base oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /code

# Instalar Poetry
RUN pip install poetry

# Verificar que Poetry está instalado correctamente
RUN poetry --version

# Copiar el archivo pyproject.toml y poetry.lock al contenedor
COPY pyproject.toml poetry.lock /code/

# Instalar las dependencias con más detalles de depuración
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi -vvv  # Agregamos -vvv para mayor detalle

# Copiar el resto del código de la aplicación
COPY . /code/

# Exponer el puerto de la aplicación
EXPOSE 8000

# Comando de arranque
CMD ["gunicorn", "infrastructure.django.wsgi:application", "-k", "gevent", "-w", "3", "-b", ":8000", "--worker-connections=1000", "--timeout=4000", "--reload", "--capture-output", "--enable-stdio-inheritance", "--log-level=debug", "--access-logfile=-", "--log-file=/var/log/error.log"]
