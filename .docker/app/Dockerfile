# Usar una imagen base oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /code

# Instalar dependencias del sistema para Poetry
RUN apt-get update && apt-get install -y curl

# Instalar Poetry utilizando el script oficial
RUN curl -sSL https://install.python-poetry.org | python3 -

# Agregar Poetry al PATH
ENV PATH="/root/.local/bin:$PATH"

# Verificar la instalación de Poetry
RUN poetry --version

# Copiar el archivo pyproject.toml y poetry.lock al contenedor
COPY pyproject.toml poetry.lock /code/

# Instalar las dependencias con Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi -vvv  # Mantener el modo verbose

# Copiar el resto del código de la aplicación
COPY . /code/

# Exponer el puerto de la aplicación
EXPOSE 8000

# Comando de arranque
CMD ["gunicorn", "infrastructure.django.wsgi:application", "-k", "gevent", "-w", "3", "-b", ":8000", "--worker-connections=1000 --timeout=4000 --reload --capture-output --enable-stdio-inheritance --log-level=debug --access-logfile=- --log-file=/var/log/error.log"]
