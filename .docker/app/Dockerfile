FROM rudodeveloper/python:3.12.0

# Instalar Poetry
RUN pip install poetry

# Crear directorio de trabajo
RUN mkdir /code
WORKDIR /code

# Copiar todos los archivos del proyecto al contenedor
COPY . /code/

# Instalar las dependencias con Poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Exponer el puerto para la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación con Gunicorn
CMD ["gunicorn", "infrastructure.django.wsgi:application", "-b", "0.0.0.0:8000", "--workers=3", "--log-level=debug"]
